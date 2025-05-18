import os
from threading import Thread

from audio_capture import audio_capture
from translate_and_synthesize import translate_and_synthesize
from voice_clone import record_voice_sample


def main():
    if not os.path.exists("speaker.wav"):
        record_voice_sample()

    audio_thread = Thread(target=audio_capture)
    translate_thread = Thread(target=translate_and_synthesize)

    audio_thread.start()
    translate_thread.start()

    audio_thread.join()
    translate_thread.join()

if __name__ == "__main__":
    main()
