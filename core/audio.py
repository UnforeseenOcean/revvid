import pyttsx3
import json


def generate_audio(title, comment_text):
    engine = pyttsx3.init()

    engine.setProperty("rate", 180)
    voices = engine.getProperty("voices")

    try:
        voice = [v for v in voices if v.name == "Daniel"][0]
    except IndexError:
        pass
    else:
        engine.setProperty("voice", voice.id)

    engine.save_to_file(title, "dump/title.mp3")

    for id, text in comment_text.items():
        engine.save_to_file(text, f"dump/audio-{id}.mp3")
        print("Generating audio for comment", id)

    engine.runAndWait()
