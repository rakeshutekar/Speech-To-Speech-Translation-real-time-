import torch
from transformers import pipeline

# Load the emotion classification pipeline once when the module is imported
_DEVICE = 0 if torch.cuda.is_available() else -1
_emotion_classifier = pipeline(
    "audio-classification",
    model="ehcalabres/wav2vec2-lg-xlsr-en-speech-emotion-recognition",
    device=_DEVICE,
)


def detect_emotion(audio_path: str) -> str:
    """Return the top emotion label for the given audio file."""
    results = _emotion_classifier(audio_path)
    if not results:
        return "neutral"
    top = max(results, key=lambda r: r["score"])
    return top["label"]
