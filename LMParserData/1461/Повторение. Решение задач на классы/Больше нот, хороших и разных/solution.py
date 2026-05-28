PITCHES = ["до", "ре", "ми", "фа", "соль", "ля", "си"]

long_notes = {
    "до": "до-о",
    "ре": "ре-э",
    "ми": "ми-и",
    "фа": "фа-а",
    "соль": "со-оль",
    "ля": "ля-а",
    "си": "си-и",
}


class Note:
    def __init__(self, note, is_long=False):
        if not is_long:
            self.note = note
        else:
            self.note = long_notes[note]

    def play(self):
        print(self.note)

    def __str__(self):
        return self.note


class LoudNote(Note):
    def __init__(self, note, is_long=False):
        super().__init__(note, is_long)
        self.note = self.note.upper()


class DefaultNote(Note):
    def __init__(self, note="до", is_long=False):
        super().__init__(note, is_long)


class NoteWithOctave(Note):
    def __init__(self, note, octave, is_long=False):
        super().__init__(note, is_long)
        self.note = f"{self.note} ({octave})"