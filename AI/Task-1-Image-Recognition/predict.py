import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageOps
from tensorflow.keras.models import load_model


MODEL_PATH = "keras_model.h5"
LABELS_PATH = "labels.txt"
IMAGE_SIZE = (224, 224)


def load_labels(labels_path):
    labels = []

    with open(labels_path, "r", encoding="utf-8") as file:
        for line in file.readlines():
            line = line.strip()

            # Teachable Machine labels usually look like:
            # 0 Screwdriver
            # 1 Wrench
            # 2 Pliers
            if " " in line:
                label = line.split(" ", 1)[1]
            else:
                label = line

            labels.append(label)

    return labels


def prepare_image(image_path):
    image = Image.open(image_path).convert("RGB")

    # Resize and crop image to 224x224
    image = ImageOps.fit(image, IMAGE_SIZE, Image.Resampling.LANCZOS)

    image_array = np.asarray(image).astype(np.float32)

    # Normalize image values from 0-255 to -1 to 1
    normalized_image_array = (image_array / 127.5) - 1

    # Create input array for the model
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    data[0] = normalized_image_array

    return data


def predict(image_path):
    if not Path(MODEL_PATH).exists():
        print(f"Error: Could not find {MODEL_PATH}")
        return

    if not Path(LABELS_PATH).exists():
        print(f"Error: Could not find {LABELS_PATH}")
        return

    if not Path(image_path).exists():
        print(f"Error: Could not find image file: {image_path}")
        return

    model = load_model(MODEL_PATH, compile=False)
    labels = load_labels(LABELS_PATH)
    image_data = prepare_image(image_path)

    prediction = model.predict(image_data)

    predicted_index = np.argmax(prediction)
    predicted_class = labels[predicted_index]
    confidence_score = prediction[0][predicted_index]

    print("Prediction Result")
    print("-----------------")
    print(f"Input Image: {image_path}")
    print(f"Predicted Class: {predicted_class}")
    print(f"Confidence Score: {confidence_score * 100:.2f}%")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:")
        print("python predict.py image_name.jpg")
        print()
        print("Example:")
        print("python predict.py test_pliers.jpg")
    else:
        image_path = sys.argv[1]
        predict(image_path)