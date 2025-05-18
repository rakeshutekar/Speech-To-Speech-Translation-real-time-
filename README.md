# Speech-To-Speech-Translation-real-time
This a Speech to Speech Translation Application which translates any-language to any-language in Real time. This application is build using Python and openai APIs
# Speech-to-Speech Translation

## Introduction

This project demonstrates a real-time speech-to-speech translation system that supports 99 languages using the [Whisper model](https://huggingface.co/openai/whisper-large-v3). The system captures audio input, translates the speech, and synthesizes the translated speech in real-time. The API-based version now includes **voice cloning** so the translated output uses the speaker's own voice.

If you don't have the required computing power to run the models locally, you can use the OpenAI API for speech-to-text and text-to-speech services. The project supports both configurations: using pre-trained models directly and using OpenAI API.

## Running Locally with OpenAI API

1. Clone the repository:
    ```sh
    git clone https://github.com/rakeshutekar/Speech-To-Speech-Translation-real-time-.git
    cd speech-to-speech-translation
    ```

2. Create a virtual environment and install dependencies:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3. Create a `.env` file in the root directory and add your OpenAI API key:
    ```
    OPENAI_API_KEY=your_openai_api_key
    ```

4. When the script starts you will be asked to record a short sample of your
   voice. This sample is used to clone your voice for speech synthesis.

5. Run the project:
    ```sh
    python main.py
    ```

## Running Locally with Pre-trained Models

1. Clone the repository:
    ```sh
    git clone https://github.com/rakeshutekar/Speech-To-Speech-Translation-real-time-.git
    cd speech-to-speech-translation
    ```

2. Create a virtual environment and install dependencies:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3. Run the project:
    ```sh
    python main.py
    ```

## Contributing

We welcome contributions from the open-source community to enhance the speech-to-speech translation system. Here are some ideas you can contribute to:

1. **Voice Cloning**: The API version already clones the speaker's voice. Further improvements are welcome. Reference models:
    - [OpenVoiceV2](https://huggingface.co/myshell-ai/OpenVoiceV2)
    - [PSST-Fairseq-Voice-Clone](https://huggingface.co/birgermoell/psst-fairseq-voice-clone)

2. **Emotion Detection**: Add emotion detection to identify the speaker's emotion. Reference model:
    - [wav2vec2-lg-xlsr-en-speech-emotion-recognition](https://huggingface.co/ehcalabres/wav2vec2-lg-xlsr-en-speech-emotion-recognition)

3. **Output Speech with Emotion**: Enhance the system to output synthesized speech with detected emotions.

## Demo

Check out the demo of the Speech-to-Speech Translator in real-time [link_to_demo_video](https://www.youtube.com/watch?v=dGcVsK-LN8A&feature=youtu.be).

## Framework
![STS api](https://github.com/rakeshutekar/Speech-To-Speech-Translation-real-time-/assets/48244158/0b8f75c1-170f-4758-84af-89b1eb9d6d02)

