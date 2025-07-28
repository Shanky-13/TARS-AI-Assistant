import pygame
import os
import eel

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
