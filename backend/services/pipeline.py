from ml.inference.yolo_inference import detect_tables
from ml.inference.trocr_detectron_inference import extract_text


def run_pipeline(file_path):

    text_result = extract_text(file_path)

    table_result = detect_tables(file_path)

    return {
        "text": text_result,
        "tables": table_result
    }