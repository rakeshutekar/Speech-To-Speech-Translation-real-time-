import queue
import time

import numpy as np
import pyaudio
from utils import audio_queue, is_speech

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
SILENCE_THRESHOLD = 2000
MAX_SILENCE_DURATION = 1

def audio_capture():
    print("Listening...")
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
    accumulated_audio = np.array([], dtype=np.int16)
    is_currently_speech = False
    last_speech_time = time.time()

    try:
        while True:
            data = stream.read(CHUNK, exception_on_overflow=False)
            audio_data = np.frombuffer(data, dtype=np.int16)
            
            if is_speech(audio_data):
                if not is_currently_speech:
                    is_currently_speech = True
                    accumulated_audio = np.array([], dtype=np.int16)
                last_speech_time = time.time()
                accumulated_audio = np.concatenate((accumulated_audio, audio_data))
            elif is_currently_speech and (time.time() - last_speech_time) <= MAX_SILENCE_DURATION:
                accumulated_audio = np.concatenate((accumulated_audio, audio_data))
            else:
                if len(accumulated_audio) > 0:
                    audio_queue.put(accumulated_audio.copy())
                    accumulated_audio = np.array([], dtype=np.int16)
                is_currently_speech = False
    finally:
        stream.stop_stream()
        stream.close()
        p.terminate()
