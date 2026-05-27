import subprocess

def run_pipeline(photo, audio, prompt, output):

    # 1. SadTalker (face motion)
    subprocess.run([
        "python", "ai_models/sadtalker/inference.py",
        "--source_image", photo,
        "--driven_audio", audio,
        "--result_dir", "outputs"
    ])

    sad_output = "outputs/result.mp4"

    # 2. Wav2Lip (lip sync)
    subprocess.run([
        "python", "ai_models/wav2lip/inference.py",
        "--face", sad_output,
        "--audio", audio,
        "--outfile", output
    ])

    # 3. GFPGAN (enhance face)
    subprocess.run([
        "python", "ai_models/gfpgan/inference.py",
        "-i", output,
        "-o", "outputs"
    ])

    # 4. Real-ESRGAN (upscale)
    subprocess.run([
        "python", "ai_models/realesrgan/inference_realesrgan.py",
        "-i", output,
        "-o", "outputs"
    ])

    return output
