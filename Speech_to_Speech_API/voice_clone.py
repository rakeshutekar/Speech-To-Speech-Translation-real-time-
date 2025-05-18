import numpy as np
import pyaudio
import soundfile as sf
import torch
from TTS.api import TTS

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100


def record_voice_sample(filename="speaker.wav", seconds=3):
    """Record a short voice sample for cloning."""
    print("Recording voice sample for voice cloning...")
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
    frames = []
    for _ in range(int(RATE / CHUNK * seconds)):
        data = stream.read(CHUNK, exception_on_overflow=False)
        frames.append(np.frombuffer(data, dtype=np.int16))
    stream.stop_stream()
    stream.close()
    p.terminate()

    audio = np.concatenate(frames)
    sf.write(filename, audio, RATE)
    print(f"Voice sample saved to {filename}")


def load_voice_clone_model():
    """Load the XTTS model used for voice cloning."""
    device = "cuda" if torch.cuda.is_available() else "cpu"
    tts = TTS(model_name="tts_models/multilingual/multi-dataset/xtts_v2")
    tts.to(device)
    return tts


def synthesize_with_clone(tts, text, speaker_wav, language="en", file_path="speech_output.wav"):
    """Synthesize speech using the cloned voice."""
    tts.tts_to_file(text=text, speaker_wav=speaker_wav, language=language, file_path=file_path)
