import pyaudio
import time
import re
import webbrowser
import pygame
import struct
import os
import subprocess
import eel
import sqlite3
from engine.command import *
from engine.config import ASSISTANT_NAME
from engine.helper import *
from urllib.parse import quote
import pywhatkit
import pvporcupine
import pyautogui as autogui



# Initialize the mixer only once globally
pygame.mixer.init()

con = sqlite3.connect("TARS.db")
cursor = con.cursor()

# Playing Assistant Sound Function


@eel.expose
def playAssistantSound():
    sound_path = os.path.abspath("www/assets/audio/startup sound.wav")
    pygame.mixer.music.load(sound_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)


@eel.expose
def playSiriWaveSound():
    sound_path = os.path.abspath("www/assets/audio/SiriWaveSound.mp3")
    pygame.mixer.music.load(sound_path)
    pygame.mixer.music.play()


def launch_app(path_or_appid):
    try:
        if path_or_appid.endswith(".exe") and os.path.isfile(path_or_appid):
            os.startfile(path_or_appid)

        elif "!" in path_or_appid:
            # For MS Store apps with entry point (AppId contains !)
            subprocess.Popen([
                "powershell",
                "Start-Process",
                f"shell:AppsFolder\\{path_or_appid}"
            ])

        elif path_or_appid.startswith("Microsoft.") or path_or_appid.count('.') >= 2:
            # UWP app without entry point (less common, fallback)
            subprocess.Popen(
                ["explorer.exe", f"shell:AppsFolder\\{path_or_appid}"])

        else:
            print(
                f"[launch_app WARNING] Unsupported format or file not found: {path_or_appid}")
            speak("Application path is not valid or supported.")

    except Exception as e:
        print(f"[launch_app ERROR] {e}")
        speak("Unable to launch the application.")


def openCommand(query):
    try:
        query = query.replace(ASSISTANT_NAME, "")
        query = query.replace("open", "")
        app_name = query.strip().lower()

        if not app_name:
            speak("Please specify an application or website to open.")
            return

        # Check in SYSTEM_COMMANDS
        cursor.execute(
            'SELECT path FROM SYSTEM_COMMANDS WHERE LOWER(name) = ?', (app_name,))
        result = cursor.fetchone()
        if result:
            speak(f"Opening {app_name}")
            launch_app(result[0])
            return

        # Check in WEB_COMMANDS
        cursor.execute(
            'SELECT url FROM WEB_COMMANDS WHERE LOWER(name) = ?', (app_name,))
        result = cursor.fetchone()
        if result:
            speak(f"Opening {app_name}")
            webbrowser.open(result[0])
            return

        # Fallback generic attempt
        speak(f"Trying to open {app_name}")
        os.system(f'start {app_name}')

    except Exception as e:
        print(f"[openCommand ERROR] {e}")
        speak("Unable to process the request at the moment!")


def PlayYouTube(query):
    search_term = extract_yt_term(query)
    speak(f"Playing {search_term} on YouTube")
    pywhatkit.playonyt(search_term)


def hotWord():
    porcupine = None
    paud = None
    audio_stream = None

    try:
        # List of hotwords to detect
        keywords = ["jarvis", "hey google", "alexa", "hey siri"]

        # Create the porcupine instance
        porcupine = pvporcupine.create(keywords=keywords)

        # Set up PyAudio stream
        paud = pyaudio.PyAudio()
        audio_stream = paud.open(
            rate=porcupine.sample_rate,
            channels=1,
            format=pyaudio.paInt16,
            input=True,
            frames_per_buffer=porcupine.frame_length
        )

        print("Listening for hotwords...")

        while True:
            pcm = audio_stream.read(
                porcupine.frame_length, exception_on_overflow=False)
            pcm_unpacked = struct.unpack_from(
                "h" * porcupine.frame_length, pcm)

            keyword_index = porcupine.process(pcm_unpacked)

            if keyword_index >= 0:
                print(f"Hotword Detected: {keywords[keyword_index]}")

                # Simulate keypress (for testing)
                autogui.keyDown("alt")
                autogui.keyDown("shift")
                autogui.press("t")
                time.sleep(0.1)
                autogui.keyUp("alt")
                autogui.keyUp("shift")

                time.sleep(2)  # Avoid repeated triggering

    except KeyboardInterrupt:
        print("Interrupted by user. Cleaning up...")
    except Exception as e:
        print(f"Error: {e}")

    finally:
        if porcupine:
            porcupine.delete()
        if audio_stream:
            audio_stream.close()
        if paud:
            paud.terminate()


def findContact(query):
    words_to_remove = [
        ASSISTANT_NAME, "jarvis", "hey google", "alexa", "hey siri",
        "make", "a", "to", "phone", "call", "send", "message", "whatsapp", "video"
    ]

    # Remove extra keywords from query
    query = remove_words(query, words_to_remove).strip().lower()

    try:
        # Search in database for contact name
        cursor.execute(
            "SELECT mobile_no FROM CONTACTS WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?",
            ('%' + query + '%', query + '%')
        )
        results = cursor.fetchall()

        if not results:
            print("No contact found.")
            return None, query

        mobile_number_str = str(results[0][0])

        if not mobile_number_str.startswith("+91"):
            mobile_number_str = "+91" + mobile_number_str

        return mobile_number_str, query

    except Exception as e:
        print(f"Error in findContact: {e}")
        return None, query


import webbrowser
import time
import pyautogui as autogui
from urllib.parse import quote

def WhatsApp(mobile_no, message, flag, name):
    if flag == "message":
        message_content = message
        TARS_message = f"Message sent successfully to {name}"

    elif flag == "call":
        TARS_message = f"Calling {name}"
        speak("Sorry, WhatsApp web calling is not supported through automation.")
        return

    else:  # Video call
        TARS_message = f"Starting Video Call with {name}"
        speak("Sorry, video calls are not supported through WhatsApp automation.")
        return

    try:
        encoded_message = quote(message_content)
        WhatsApp_url = f"https://wa.me/{mobile_no.replace('+', '')}?text={encoded_message}"
        webbrowser.open(WhatsApp_url)

        time.sleep(7)  # Wait for WhatsApp Web to load
        autogui.press('enter')  # Press Enter to send the message

        speak(TARS_message)

    except Exception as e:
        print(f"Error in WhatsApp(): {e}")
        speak("Sorry, I couldn't complete the WhatsApp operation.")

