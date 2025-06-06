import os
import time

import openai
import soundfile as sf
from dotenv import load_dotenv
from utils import audio_queue, calculate_rms, play_audio
from audio_capture import RATE
from voice_clone import load_voice_clone_model, synthesize_with_clone

speaker_sample = os.getenv("SPEAKER_WAV", "speaker.wav")
tts_model = load_voice_clone_model()

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def translate_and_synthesize():
    while True:
        audio_data = audio_queue.get()
        if audio_data.size == 0:
            continue

        rms_energy = calculate_rms(audio_data)
        if rms_energy < 10:
            print("Audio data is too quiet, likely not speech. Skipping...")
            continue

        audio_file_path = '/tmp/audio_chunk.wav'
        sf.write(audio_file_path, audio_data, RATE)

        with open(audio_file_path, "rb") as audio_file:
            translation = openai.audio.translations.create(
                model="whisper-1", 
                file=audio_file
            )
            translated_text = translation.text
            print("Translated Text:", translated_text)

            speech_file_path = "speech_output.wav"
            prev_mod_time = os.path.getmtime(speech_file_path) if os.path.exists(speech_file_path) else 0

            try:
                synthesize_with_clone(tts_model, translated_text, speaker_sample, file_path=speech_file_path)

                new_mod_time = os.path.getmtime(speech_file_path)
                if new_mod_time > prev_mod_time:
                    print("New speech synthesized, playing audio.")
                    play_audio(speech_file_path)
                else:
                    print("No new speech synthesized, skipping playback.")

            except Exception as e:
                print(f"Error in speech synthesis: {e}")
