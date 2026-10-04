# MediScan AI demo

A small FastAPI demo for uploading a medicine-package image. **It does not currently include a trained or validated medicine-authentication model.** The API validates an image upload and responds that analysis is unavailable. It never labels a medicine genuine, fake, expired, or safe.

Do not use this demo to make medication decisions. Verify products with a licensed pharmacist or the manufacturer.

## Run locally

```bash
python -m venv .venv
# Activate the environment, then:
pip install -r requirements.txt
uvicorn app:app --reload
```

Open `http://127.0.0.1:8000`. The API limits uploads to 5 MB and accepts JPEG, PNG, and WebP images. `/health` reports service availability; `/scan` returns HTTP 503 until a verified model is configured.
