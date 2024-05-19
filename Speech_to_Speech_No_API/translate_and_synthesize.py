import os
import time

import librosa
import numpy as np
import soundfile as sf
import torch
from transformers import (AutoModelForSpeechSeq2Seq, AutoProcessor, BarkModel,
                          BarkProcessor)
from utils import audio_queue, calculate_rms, play_audio

# Load Whisper model and processor
processor = AutoProcessor.from_pretrained("openai/whisper-large-v3")
model = AutoModelForSpeechSeq2Seq.from_pretrained("openai/whisper-large-v3")

# Load Bark model and processor
bark_processor = BarkProcessor.from_pretrained("suno/bark")
bark_model = BarkModel.from_pretrained("suno/bark")

def translate_and_synthesize():
    while True:
        audio_data = audio_queue.get()
        if audio_data.size == 0:
            continue

        rms_energy = calculate_rms(audio_data)
        if rms_energy < 10:
            continue

        audio_file_path = '/tmp/audio_chunk.wav'
        sf.write(audio_file_path, audio_data, 16000)

        waveform, sampling_rate = librosa.load(audio_file_path, sr=16000)

        inputs = processor(waveform, sampling_rate=sampling_rate, return_tensors="pt")
        input_features = inputs.input_features

        device = "cuda" if torch.cuda.is_available() else "cpu"
        model.to(device)
        input_features = input_features.to(device)

        with torch.no_grad():
            predicted_ids = model.generate(input_features)

        transcription = processor.batch_decode(predicted_ids, skip_special_tokens=True)[0]
        print("Translated Text:", transcription)

        bark_inputs = bark_processor(transcription, voice_preset="v2/en_speaker_6")
        audio_array = bark_model.generate(**bark_inputs)
        audio_array = audio_array.cpu().numpy().squeeze()

        speech_file_path = "speech_output.wav"
        sf.write(speech_file_path, audio_array, 16000)

        play_audio(speech_file_path)
