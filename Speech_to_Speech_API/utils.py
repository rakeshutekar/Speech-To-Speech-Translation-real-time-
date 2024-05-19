import queue
import time

import numpy as np
import pygame

audio_queue = queue.Queue()

def is_speech(audio_data, threshold=2000):
    return np.max(np.abs(audio_data)) > threshold

def calculate_rms(audio_data):
    return np.sqrt(np.mean(np.square(audio_data), axis=-1))

def play_audio(file_path):
    pygame.mixer.music.load(str(file_path))
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

# Initialize Pygame for audio playback
pygame.init()
pygame.mixer.init()
