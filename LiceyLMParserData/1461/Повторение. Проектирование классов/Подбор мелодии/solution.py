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


class Melody:
    def __init__(self, notes=[]):
        self.notes = notes.copy()

    def __str__(self):
        melody_text = ""
        for i, note in enumerate(self.notes):
            melody_text += f"{note.note}{", " if i + 1 != len(self.notes) else ""}"
        if melody_text:
            melody_text = melody_text[0].upper() + melody_text[1:]
            return melody_text
        else:
            return ""

    def append(self, note):
        self.notes.append(note)

    def replace_last(self, note):
        if len(self.notes) > 0:
            self.notes[len(self.notes) - 1] = note
        else:
            self.notes.append(note)

    def remove_last(self):
        if len(self.notes) > 0:
            self.notes.pop(len(self.notes) - 1)

    def clear(self):
        self.notes = []

    def __len__(self):
        return len(self.notes)

    def __rshift__(self, n):
        new_notes = self.notes.copy()
        for i, note in enumerate(new_notes):
            if note.note_index + n >= N:
                new_notes = self.notes.copy()
                break
            new_notes[i] = note >> n
        return Melody(new_notes)

    def __lshift__(self, n):
        new_notes = self.notes.copy()
        for i, note in enumerate(new_notes):
            if note.note_index - n < 0:
                new_notes = self.notes.copy()
                break
            new_notes[i] = note << n
        return Melody(new_notes)