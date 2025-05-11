# app/translate.py

from googletrans import Translator

def translate_text(text, dest_lang='es'):
    translator = Translator()
    try:
        result = translator.translate(text, dest=dest_lang)
        print("🌐 Translated:", result.text)
        return result.text
    except Exception as e:
        print(f"⚠️ Translation error: {e}")
        return None
