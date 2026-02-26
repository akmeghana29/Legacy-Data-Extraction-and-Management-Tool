from fastapi import APIRouter, UploadFile, File
import os
import shutil
from backend.services.ocr_service import extract_text
from backend.services.yolo_service import detect_tables

router = APIRouter()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/extract/text")
async def extract_text_route(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = extract_text(file_path)

    return {
        "filename": file.filename,
        "text": text
    }


@router.post("/extract/table")
async def extract_table_route(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    tables = detect_tables(file_path)

    return {
        "filename": file.filename,
        "tables": tables
    }