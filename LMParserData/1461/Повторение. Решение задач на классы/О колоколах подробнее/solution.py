class BellTower:
    def __init__(self, *args):
        self.all_elements = args

    def sound(self):
        for element in self.all_elements:
            print(element.sound())
        print("...")

    def append(self, element):
        self.all_elements = self.all_elements + (element,)


class Bell:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def print_info(self):
        kwargs = [
            (f"{el[0]}: {el[1]}" if isinstance(el, tuple) else el)
            for el in sorted(self.kwargs.items(), key=lambda x: f"{x[0]}: {x[1]}")
        ]
        args = list(self.args)
        if kwargs or args:
            params_text = ", ".join(kwargs) if kwargs else ""
            if kwargs and args:
                params_text += "; "
            params_text += ", ".join(args) if args else ""
            print(params_text)
        else:
            print("-")


class LittleBell(Bell):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def sound(self):
        print("ding")


class BigBell(Bell):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.isDing = True

    def sound(self):
        if self.isDing:
            self.isDing = False
            print("ding")
        else:
            self.isDing = True
            print("dong")