def build_music_prompt(mode, user_prompt):
    base = f"You are a music assistant. Generate a {mode} pattern for an electronic music loop over 8 beats."
    details = {
        "melody": "Respond with a single line starting with:\nmelody: followed by note-duration pairs, e.g. A4(1/4) B4(1/4) C5(1/2).\nThe total duration should cover approximately 8 beats.",
        "chords": "Respond with a single line starting with:\nchords: followed by chords written like A3 C4 E4(1), separated by |.\nEach chord should last ~1 beat, for a total of 8 chords.",
    }
    style = (
        f"Style/mood requested: {user_prompt}"
        if user_prompt
        else "Style: electronic, A minor"
    )
    return f"{base}\n{details[mode]}\n{style}"
