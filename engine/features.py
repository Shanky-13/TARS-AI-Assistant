import pygame
import os
import eel
from engine.command import *
from engine.config import ASSISTANT_NAME
import pywhatkit

# Initialize the mixer only once globally
pygame.mixer.init()

# Playing Assistant Sound Function
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

def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "")
    query.lower()
    
    if query != "":
        speak(f"Opening {query}")
        os.system(f'start {query}')
        
    else:
        speak("Please specify what you want to open.")  