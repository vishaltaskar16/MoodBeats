import kagglehub
import os
import librosa
import numpy as np
import json
from tensorflow.keras.utils import to_categorical
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPool2D, Dropout, Flatten, Dense
from utils import extract_mfcc

# -----------------------------
# DOWNLOAD DATASETS
# -----------------------------
path_ravdess = kagglehub.dataset_download("uwrfkaggler/ravdess-emotional-speech-audio")
path_crema = kagglehub.dataset_download("ejlok1/cremad")

print("RAVDESS:", path_ravdess)
print("CREMA-D:", path_crema)

# -----------------------------
# LOAD AUDIO FILES
# -----------------------------
def load_ravdess(path):
    emotions = {
        '01': 'neutral',
        '02': 'calm',
        '03': 'happy',
        '04': 'sad',
        '05': 'angry',
        '06': 'fearful',
        '07': 'disgust',
        '08': 'surprised'
    }

    X, y = [], []

    for root, _, files in os.walk(path):
        for file in files:
            if file.endswith(".wav"):
                emotion_code = file.split("-")[2]
                emotion = emotions.get(emotion_code)

                mfcc = extract_mfcc(os.path.join(root, file))
                X.append(mfcc)
                y.append(emotion)

    return X, y


def load_cremad(path):
    emotions = {
        "ANG": "angry",
        "DIS": "disgust",
        "FEA": "fearful",
        "HAP": "happy",
        "NEU": "neutral",
        "SAD": "sad"
    }

    X, y = [], []

    for file in os.listdir(path):
        if file.endswith(".wav"):
            emotion_code = file.split('_')[2]
            emotion = emotions.get(emotion_code)

            mfcc = extract_mfcc(os.path.join(path, file))
            X.append(mfcc)
            y.append(emotion)

    return X, y


# -----------------------------
# MERGE DATASETS
# -----------------------------
X1, y1 = load_ravdess(path_ravdess)
X2, y2 = load_cremad(path_crema)

X = np.array(X1 + X2)
y = np.array(y1 + y2)

print("Total Samples:", len(X))

# -----------------------------
# ENCODE OUTPUT LABELS
# -----------------------------
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)
y_categorical = to_categorical(y_encoded)

# Save labels
with open("labels.json", "w") as f:
    json.dump(list(label_encoder.classes_), f, indent=2)

# -----------------------------
# TRAIN TEST SPLIT
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y_categorical, test_size=0.2, random_state=42
)

# -----------------------------
# CNN MODEL (2D)
# -----------------------------
model = Sequential()

model.add(Conv2D(64, (3,3), activation='relu', input_shape=(40,150,1)))
model.add(MaxPool2D((2,2)))
model.add(Dropout(0.3))

model.add(Conv2D(128, (3,3), activation='relu'))
model.add(MaxPool2D((2,2)))
model.add(Dropout(0.3))

model.add(Flatten())
model.add(Dense(256, activation='relu'))
model.add(Dropout(0.3))

model.add(Dense(y_categorical.shape[1], activation='softmax'))

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.summary()

# -----------------------------
# TRAINING
# -----------------------------
history = model.fit(
    X_train, y_train,
    validation_data=(X_test, y_test),
    epochs=25,
    batch_size=32
)

# -----------------------------
# SAVE MODEL
# -----------------------------
model.save("model.h5")
print("Model saved successfully.")
