# app/tts.py

from gtts import gTTS
import playsound
import uuid
import os

TEMP_DIR = "temp"

def speak_text(text, lang='hi'):
    if not os.path.exists(TEMP_DIR):
        os.makedirs(TEMP_DIR)

    filename = os.path.join(TEMP_DIR, f"{uuid.uuid4()}.mp3")
    try:
        tts = gTTS(text=text, lang=lang)
        tts.save(filename)
        playsound.playsound(filename)
    except Exception as e:
        print(f"⚠️ TTS error: {e}")
    finally:
        if os.path.exists(filename):
            os.remove(filename)
