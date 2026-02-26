from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
import shutil
import os
from services.trocr_service import extract_text_from_image
from services.yolo_service import detect_tables

router = APIRouter()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/extract-text")
async def extract_text(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = extract_text_from_image(file_path)

    return JSONResponse({
        "filename": file.filename,
        "extracted_text": text
    })


@router.post("/extract-tables")
async def extract_tables(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    tables = detect_tables(file_path)

    return JSONResponse({
        "filename": file.filename,
        "tables": tables
    })