class BellTower:
    def __init__(self, *args):
        self.all_elements = args

    def sound(self):
        for element in self.all_elements:
            print(element.sound())
        print("...")

    def append(self, element):
        self.all_elements = self.all_elements + (element,)


class LittleBell:
    def sound(self):
        return "ding"


class BigBell:
    def __init__(self):
        self.isDing = True

    def sound(self):
        if self.isDing:
            self.isDing = False
            return "ding"
        else:
            self.isDing = True
            return "dong"