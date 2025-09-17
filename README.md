# Text2Mid

**Text2Mid** is a Python application designed to convert user-defined musical preferences into MIDI files. It automatically generates personalized musical sequences based on text descriptions.

## What is MIDI?

MIDI (Musical Instrument Digital Interface) is a standardized protocol for communicating digital musical information, such as notes played, their duration, velocity, and more. A MIDI file does not contain actual audio but instructions that electronic instruments or software can use to reproduce music.

## Features

- Easy input of musical preferences (style, tempo, genre, number of notes, chords, etc.)
- Automatic generation of melodies and chords as MIDI files
- Advanced use of the Gemini 2.5 Flash model for intelligent generation
- MIDI synthesis and manipulation using the `pretty_midi` library
- Interactive web interface built with Streamlit

## Technologies Used

- **Python**: main programming language of the project
- **Streamlit**: for creating the intuitive web user interface
- **Gemini 2.5 Flash**: AI model used for music sequence generation
- **pretty_midi**: Python library for reading, writing, and manipulating MIDI files

## Installation

```bash
pip install streamlit pretty_midi music21 google-generativeai
