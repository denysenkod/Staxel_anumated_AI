from elevenlabs import ElevenLabs
import os
import base64

def save_base64_audio(audio_base64: str, filename: str = "output.mp3"):
    output_dir = "."
    output_file = "audio.mp3"
    output_path = os.path.join(output_dir, output_file)

    os.makedirs(output_dir, exist_ok=True)

    with open(output_path, "wb") as f:
        f.write(base64.b64decode(audio_base64))

    print(f"✅ Audio saved to {filename}")