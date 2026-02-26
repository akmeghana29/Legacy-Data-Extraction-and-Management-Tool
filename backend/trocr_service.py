import torch
from PIL import Image
import cv2
import numpy as np
from transformers import TrOCRProcessor, VisionEncoderDecoderModel
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from detectron2 import model_zoo

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TROCR_PATH = os.path.join(BASE_DIR, "../ml_models/trocr/")
DETECTRON_PATH = os.path.join(BASE_DIR, "../ml_models/detectron/model_final.pth")
DETECTRON_CONFIG = os.path.join(BASE_DIR, "../ml_models/detectron/config.yaml")

processor = TrOCRProcessor.from_pretrained(TROCR_PATH)
trocr_model = VisionEncoderDecoderModel.from_pretrained(TROCR_PATH)

cfg = get_cfg()
cfg.merge_from_file(DETECTRON_CONFIG)
cfg.MODEL.WEIGHTS = DETECTRON_PATH
cfg.MODEL.DEVICE = "cpu"

detectron = DefaultPredictor(cfg)


def extract_text_from_image(image_path):

    image = cv2.imread(image_path)

    outputs = detectron(image)

    boxes = outputs["instances"].pred_boxes.tensor.cpu().numpy()

    lines = []

    for box in boxes:

        x1, y1, x2, y2 = map(int, box)

        cropped = image[y1:y2, x1:x2]

        pil_image = Image.fromarray(cv2.cvtColor(cropped, cv2.COLOR_BGR2RGB))

        pixel_values = processor(images=pil_image, return_tensors="pt").pixel_values

        with torch.no_grad():
            generated_ids = trocr_model.generate(pixel_values)

        text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]

        lines.append(text)

    return "\n".join(lines)