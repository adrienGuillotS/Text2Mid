# streamlit_app.py
import streamlit as st
import tempfile
import os

from midi_generator import generate_midi_from_text
from llm_generator import build_music_prompt, call_gemini
from utils import key

st.title("Text2🎶Mid")

mode = st.selectbox("Choose what to generate:", ["melody", "chords"])

bpm = st.slider("Select BPM:", min_value=60, max_value=200, value=130)

key = st.selectbox(
    "Select Key:",
    key,
)

styles = [
    "Uplifting",
    "Dark",
    "Euphoric",
    "Melancholic",
    "Aggressive",
    "Chill",
    "Happy",
    "Sad",
    "Energetic",
    "Calm",
]
genres = [
    "Trance",
    "House",
    "Techno",
    "Drum & Bass",
    "Ambient",
    "Lo-Fi",
    "Pop",
    "Rock",
    "Jazz",
    "Classical",
    "Hip-Hop",
    "R&B",
]
genres, styles = sorted(genres), sorted(styles)

style = st.selectbox("Select Style:", styles)
genre = st.selectbox("Select Genre:", genres)
num_chords = 8
num_notes = 8
if mode == "chords":
    num_chords = st.slider("Number of chords per measure:", 1, 16, 8)

else:
    num_notes = st.slider("Number of notes per measure:", 1, 16, 8)

num_measures = st.slider("Number of measures:", 1, 8, 2)


user_prompt = st.text_input(
    "Additional description (optional)", placeholder="e.g. euphoric trance in A minor"
)

if st.button("Generate MIDI"):
    with st.spinner("Generating music..."):
        full_prompt = build_music_prompt(
            mode,
            key,
            bpm,
            style,
            genre,
            user_prompt,
            num_chords,
            num_notes,
            num_measures,
        )
        llm_output = call_gemini(full_prompt)
        st.text_area("raw output:", llm_output, height=150)

        with tempfile.NamedTemporaryFile(delete=False, suffix=".mid") as tmpfile:
            output_path = tmpfile.name
            generate_midi_from_text(
                llm_output, output_file=output_path, mode=mode, bpm=bpm
            )

        with open(output_path, "rb") as f:
            st.download_button(
                "Download MIDI",
                f,
                file_name=f"{mode}_{key}_loop_{bpm}bpm.mid",
                mime="audio/midi",
            )

        os.remove(output_path)
