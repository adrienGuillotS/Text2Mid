import pretty_midi
from music21 import chord, harmony, pitch


def note_to_midi(note_str):
    """
    Convertit une note en string (ex: "C4", "A#3") en pitch MIDI (int).
    """
    try:
        p = pitch.Pitch(note_str)
        return p.midi
    except Exception:
        raise ValueError(f"Note invalide : {note_str}")


def generate_midi_from_text(text, output_file="output.mid", mode="melody", bpm=120):
    midi = pretty_midi.PrettyMIDI()
    instrument = pretty_midi.Instrument(program=0, name=mode)
    time = 0.0

    # Trouve la bonne ligne
    line = next(
        (l for l in text.strip().splitlines() if l.startswith(mode + ":")), None
    )
    if not line:
        raise ValueError(f"No {mode} line found.")

    content = line.split(":", 1)[1].strip()
    print(content)

    if mode == "melody":
        tokens = content.split()
        for token in tokens:
            try:
                note, dur = token.strip().split("(")
                dur = float(dur.strip(")").split("/")[0]) / float(
                    dur.strip(")").split("/")[1]
                )
                pitch = note_to_midi(note)
                note_obj = pretty_midi.Note(
                    velocity=100, pitch=pitch, start=time, end=time + dur
                )
                instrument.notes.append(note_obj)
                time += dur
            except:
                continue

    elif mode == "chords":
        chords = content.split("|")
        for chord_token in chords:
            chord_token = chord_token.strip()
            if not chord_token:
                continue
            try:

                if "(" in chord_token and ")" in chord_token:
                    name_part = chord_token.split("(")[0].strip()
                    duration = float(chord_token.split("(")[1].replace(")", "").strip())
                else:
                    name_part = chord_token
                    duration = 1.0  # par défaut

                # ✅ Crée l'accord
                parsed_chord = harmony.ChordSymbol(name_part)
                notes = parsed_chord.pitches

                # 🎹 Ajoute les notes MIDI avec la bonne durée
                for n in notes:
                    midi_pitch = n.midi
                    note_obj = pretty_midi.Note(
                        velocity=100, pitch=midi_pitch, start=time, end=time + duration
                    )
                    instrument.notes.append(note_obj)
                time += duration

            except Exception as e:
                print(f"Skipping chord {chord_token}: {e}")

    midi.instruments.append(instrument)
    midi.write(output_file)
    return output_file
