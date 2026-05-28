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
    def __init__(self, note, long=False):
        if not long:
            self.note = note
        else:
            self.note = long_notes[note]

    def play(self):
        print(self.note)

    def __str__(self):
        return self.note