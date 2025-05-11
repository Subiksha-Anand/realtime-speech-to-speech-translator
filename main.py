# main.py

from app.speech import recognize_speech
from app.translate import translate_text
from app.tts import speak_text

def speech_to_speech(dest_lang='es'):
    print(f"🌍 Starting speech-to-speech translation to '{dest_lang}'...")
    while True:
        input_text = recognize_speech()
        if input_text:
            translated = translate_text(input_text, dest_lang)
            if translated:
                speak_text(translated, lang=dest_lang)

if __name__ == "__main__":
    speech_to_speech(dest_lang='hi')  # Change to any supported language code
