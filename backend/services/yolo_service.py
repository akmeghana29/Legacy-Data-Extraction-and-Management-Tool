import os
from ultralytics import YOLO

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

YOLO_MODEL_PATH = os.path.join(BASE_DIR, "../ml_models/yolo/best.pt")

model = YOLO(YOLO_MODEL_PATH)

CLASS_NAMES = ['cell', 'row', 'table']


def detect_tables(image_path):

    results = model.predict(
        source=image_path,
        conf=0.25,
        save=False,
        verbose=False
    )

    detections = []

    for result in results:

        for box in result.boxes:

            cls_id = int(box.cls[0])
            conf = float(box.conf[0])

            x1, y1, x2, y2 = map(int, box.xyxy[0])

            detections.append({
                "class_id": cls_id,
                "class_name": CLASS_NAMES[cls_id],
                "confidence": conf,
                "bbox": {
                    "x1": x1,
                    "y1": y1,
                    "x2": x2,
                    "y2": y2
                }
            })

    return detections