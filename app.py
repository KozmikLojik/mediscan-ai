from __future__ import annotations

from io import BytesIO
from pathlib import Path

from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.responses import FileResponse
from PIL import Image, UnidentifiedImageError

MAX_UPLOAD_BYTES = 5 * 1024 * 1024
MAX_IMAGE_DIMENSION = 8_000
STATIC_DIR = Path(__file__).resolve().parent / "static"

app = FastAPI(title="MediScan AI demo", version="0.1.0")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "analysis": "unavailable"}


@app.get("/", include_in_schema=False)
def home() -> FileResponse:
    return FileResponse(STATIC_DIR / "index.html")


@app.post("/scan")
async def scan_medicine_image(file: UploadFile = File(...)) -> None:
    content = await file.read(MAX_UPLOAD_BYTES + 1)
    await file.close()
    if not content:
        raise HTTPException(status_code=400, detail="Choose an image to continue.")
    if len(content) > MAX_UPLOAD_BYTES:
        raise HTTPException(status_code=413, detail="The image must be 5 MB or smaller.")

    try:
        with Image.open(BytesIO(content)) as image:
            if image.format not in {"JPEG", "PNG", "WEBP"}:
                raise HTTPException(status_code=415, detail="Use a JPEG, PNG, or WebP image.")
            if max(image.size) > MAX_IMAGE_DIMENSION:
                raise HTTPException(status_code=413, detail="The image dimensions are too large.")
            image.verify()
    except HTTPException:
        raise
    except (UnidentifiedImageError, OSError, Image.DecompressionBombError) as error:
        raise HTTPException(status_code=400, detail="The uploaded file is not a valid image.") from error

    # This repository does not contain trained or validated medicine-authentication weights.
    # Never return a fabricated genuine/fake classification or medical safety advice.
    raise HTTPException(
        status_code=503,
        detail=(
            "Medicine analysis is not available yet: no verified model is configured. "
            "Do not use this demo to decide whether a medicine is genuine or safe. "
            "Ask a licensed pharmacist or contact the manufacturer."
        ),
    )
