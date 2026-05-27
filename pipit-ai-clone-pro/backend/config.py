import os

# =========================
# PIPIT AI CONFIGURATION
# =========================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

UPLOAD_DIR = os.path.join(BASE_DIR, "..", "uploads")
OUTPUT_DIR = os.path.join(BASE_DIR, "..", "outputs")

# =========================
# AI MODEL PATHS
# =========================

SADTALKER_PATH = os.path.join(BASE_DIR, "ai_models", "sadtalker")
WAV2LIP_PATH = os.path.join(BASE_DIR, "ai_models", "wav2lip")
GFPGAN_PATH = os.path.join(BASE_DIR, "ai_models", "gfpgan")
REALESRGAN_PATH = os.path.join(BASE_DIR, "ai_models", "realesrgan")

# =========================
# VIDEO SETTINGS
# =========================

MAX_VIDEO_DURATION = 30  # seconds
FPS = 25
RESOLUTION = "1280x720"

# =========================
# AI PIPELINE SETTINGS
# =========================

USE_GPU = True
ENABLE_FACE_ENHANCEMENT = True
ENABLE_UPSCALE = True

# =========================
# TEMP FILE SETTINGS
# =========================

TEMP_CLEANUP = True
KEEP_ORIGINALS = False

# =========================
# SERVER SETTINGS
# =========================

HOST = "0.0.0.0"
PORT = 8000

# =========================
# SECURITY (optional for later SaaS)
# =========================

API_KEY_REQUIRED = False
API_SECRET = "change_this_later"
