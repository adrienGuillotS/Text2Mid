# gemini_llm.py

import os
from dotenv import load_dotenv
import google.generativeai as genai

from utils import all_chords

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")


def build_music_prompt(
    mode, key, bpm, style, genre, user_prompt, num_chords=8, num_notes=8, num_measures=1
):
    base = f"You are a music assistant. Generate a {mode} pattern for a music loop at {bpm} BPM."
    if mode == "melody":
        details = (
            "Respond with a single line starting with:\n"
            "melody: followed by note-duration pairs like A4(1/4) B4(1/2) C5(1). "
            f"The total duration should be {num_measures} measures. "
            f"Try to include around {num_notes} different notes, but the priority is to fill the full duration. "
        )
    else:

        details = (
            f"Respond with a single line starting with:\n"
            f"chords: followed by {num_chords} chords written like Cmaj7(1) | Gmaj7(1), "
            f"where the number in parentheses represents the duration in beats for each chord. "
            f"The total duration should be {num_measures} measures. "
            f"Use standard chord in the list : {all_chords}."
            f"Try to include around {num_chords} different chords, but the priority is to fill the full duration. "
        )
    style_key_genre = f"Style: {style},Key: {key}, Genre: {genre}"
    user_style = f"User description: {user_prompt}" if user_prompt else ""
    return f"{base}\n{details}\n{style_key_genre}\n{user_style}"


def call_gemini(prompt):
    response = model.generate_content(prompt)
    return response.text.strip()
