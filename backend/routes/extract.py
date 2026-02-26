from fastapi import APIRouter, UploadFile, File
import os
import shutil

from backend.services.pipeline import run_pipeline
from backend.config import UPLOAD_DIR


router = APIRouter()


@router.post("/extract")
async def extract(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = run_pipeline(file_path)

    return result