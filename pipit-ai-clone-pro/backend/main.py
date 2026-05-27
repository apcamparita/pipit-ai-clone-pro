from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import os
import uuid
from pipeline import run_pipeline

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD = "uploads"
OUTPUT = "outputs"

os.makedirs(UPLOAD, exist_ok=True)
os.makedirs(OUTPUT, exist_ok=True)

@app.post("/generate")
async def generate(
    photo: UploadFile = File(...),
    audio: UploadFile = File(...),
    prompt: str = Form(...)
):

    uid = str(uuid.uuid4())

    photo_path = f"{UPLOAD}/{uid}.png"
    audio_path = f"{UPLOAD}/{uid}.wav"
    output_path = f"{OUTPUT}/{uid}.mp4"

    with open(photo_path, "wb") as f:
        f.write(await photo.read())

    with open(audio_path, "wb") as f:
        f.write(await audio.read())

    video = run_pipeline(photo_path, audio_path, prompt, output_path)

    return FileResponse(video, media_type="video/mp4")
