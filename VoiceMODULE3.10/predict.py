import numpy as np
import json
import librosa
from tensorflow.keras.models import load_model
from utils import extract_mfcc

# Load model & labels
model = load_model("model.h5")

with open("labels.json", "r") as f:
    labels = json.load(f)

def predict_emotion(file_path):
    mfcc = extract_mfcc(file_path)
    mfcc = np.expand_dims(mfcc, axis=0)

    pred = model.predict(mfcc)
    emotion = labels[np.argmax(pred)]
    confidence = float(np.max(pred))

    return emotion, confidence
