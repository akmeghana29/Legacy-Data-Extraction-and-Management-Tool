import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODELS_DIR = os.path.join(BASE_DIR, "..", "ml", "models")

YOLO_MODEL_PATH = os.path.join(MODELS_DIR, "yolo", "best.pt")
TROCR_MODEL_PATH = os.path.join(MODELS_DIR, "trocr")
DETECTRON_MODEL_PATH = os.path.join(MODELS_DIR, "detectron")

UPLOAD_DIR = os.path.join(BASE_DIR, "uploads")
OUTPUT_DIR = os.path.join(BASE_DIR, "outputs")

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)