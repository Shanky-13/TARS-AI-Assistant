import pyttsx3
import speech_recognition as sr
import eel
import time


def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 174)
    eel.DisplayMessage(text)
    engine.say(text)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        eel.DisplayMessage("Listening...")
        r.adjust_for_ambient_noise(source, duration=0.5)

        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=4)
        except sr.WaitTimeoutError:
            eel.DisplayMessage("Timed out, no speech detected.")
            return "listening timed out..."

    try:
        eel.DisplayMessage("Recognizing...")
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

        # Display the actual recognized message
        eel.DisplayMessage(query)

        # Give UI a moment to render before speaking
        time.sleep(1)

        return query.lower()

    except sr.UnknownValueError:
        eel.DisplayMessage("Sorry, could not understand.")
        return "say that again please..."

    except sr.RequestError:
        eel.DisplayMessage("Network error.")
        return "speech service unavailable"

    except Exception as e:
        eel.DisplayMessage("An error occurred.")
        print(f"Error: {e}")
        return ""


@eel.expose
def allCommands(message = 1):
    
    if message == 1:
        query = takeCommand()
        print(f"[User Command] {query}")
        
    else:
        query = message
    
    try:
    
        if "open" in query:
            from engine.features import openCommand
            openCommand(query)

        elif "on youtube" in query:
            from engine.features import PlayYouTube
            PlayYouTube(query)

        elif "send message" in query or "phone call" in query or "video call" in query:
            from engine.features import findContact, WhatsApp
            message = ""
            mobile_no, name = findContact(query)

            if mobile_no != 0:
                if "send message" in query:
                    flag = "message"
                    speak("What's the message?")
                    message = takeCommand()

                elif "phone call" in query:
                    flag = "call"
                    message = ""  # No message needed for call

                else:
                    flag = "video"
                    message = ""  # No message needed for video call

                WhatsApp(mobile_no, message, flag, name)

        else:
            message = "I didn't understand that command. Please try again."
            eel.DisplayMessage(message)
            speak(message)

    except Exception as e:
        print(f"[allCommands ERROR] {e}")
        eel.DisplayMessage(
            "Something went wrong while processing your command.")
        speak("Something went wrong while processing your command.")

    eel.ShowHood()
