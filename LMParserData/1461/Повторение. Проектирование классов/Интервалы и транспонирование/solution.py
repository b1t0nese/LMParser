N = 7
PITCHES = ["до", "ре", "ми", "фа", "соль", "ля", "си"]
LONG_PITCHES = ["до-о", "ре-э", "ми-и", "фа-а", "со-оль", "ля-а", "си-и"]
INTERVALS = ["прима", "секунда", "терция", "кварта", "квинта", "секста", "септима"]


class Note:
    def __init__(self, note, is_long=False):
        self.is_long = is_long
        self.note_index = PITCHES.index(note) if note in PITCHES else LONG_PITCHES.index(note)
        self.note = self.pitches()[self.note_index]

    def pitches(self):
        return PITCHES if not self.is_long else LONG_PITCHES

    def play(self):
        print(self.note)

    def __str__(self):
        return self.note

    def __eq__(self, other):
        return self.note_index == other.note_index

    def __lt__(self, other):
        return self.note_index < other.note_index

    def __le__(self, other):
        return self.note_index <= other.note_index

    def __rshift__(self, other):
        return Note(self.pitches()[(self.note_index + other) % N], self.is_long)

    def __lshift__(self, other):
        return Note(self.pitches()[(self.note_index - other) % N], self.is_long)

    def get_interval(self, other):
        return INTERVALS[abs(self.note_index - other.note_index)]


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