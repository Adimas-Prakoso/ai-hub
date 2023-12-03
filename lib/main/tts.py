from gtts import gTTS
import os

def text_to_speech(text, language='en', output_file='output.mp3'):
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save(output_file)
    os.system("start " + output_file)  # Buka file audio dengan program default pada sistem