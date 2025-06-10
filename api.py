import torch
from TTS.api import TTS
from flask import Flask, request, send_file
import torchaudio
import io
from threading import Lock

app = Flask(__name__)
lock = Lock()

# Initialize TTS model
device = "cuda" if torch.cuda.is_available() else "cpu"
tts_model = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)

@app.route("/")
def home():
    print("HELLO")
    return "API HEREE JUHUU"

@app.route("/api/tts", methods=["POST"])
def text_to_speech():
    with lock:
        try:
            # Get parameters
            text = request.form.get("text", "")
            if not text:
                return "No text provided", 400

            if 'speaker_wav' not in request.files:
                return "No speaker reference provided", 400

            speaker_file = request.files['speaker_wav']

            # Save temporary file (or process directly from memory)
            temp_path = "/tmp/reference_audio.wav"
            speaker_file.save(temp_path)

            # Generate audio
            print(f" > Model input: {text}")
            tts_model.tts_to_file(
                text=text,
                speaker_wav=temp_path,
                language="en",
                file_path="output.wav"
            )

            # Convert to bytes
            with open("output.wav", "rb") as f:
                out = io.BytesIO(f.read())

            return send_file(out, mimetype="audio/wav", as_attachment=True, download_name="output.wav")

        except Exception as e:
            print(f"Error in TTS: {str(e)}")
            return f"TTS Error: {str(e)}", 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002)
