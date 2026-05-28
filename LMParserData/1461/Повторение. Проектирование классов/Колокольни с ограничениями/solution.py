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
        return "ding"


class BigBell(Bell):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.isDing = True

    def sound(self):
        if self.isDing:
            self.isDing = False
            return "ding"
        self.isDing = True
        return "dong"


class BellTower:
    def __init__(self, *args):
        self.bells = list(args)

    def append(self, bell):
        self.bells.append(bell)

    def sound(self):
        for bell in self.bells:
            print(bell.sound())
        print("...")

    def print_info(self):
        for i, bell in enumerate(self.bells, 1):
            print(i, bell.__class__.__name__)
            bell.print_info()
        print()


class SizedBellTower(BellTower):
    def __init__(self, *args, size=10):
        super().__init__(*args[-size:])
        self.size = size

    def append(self, bell):
        super().append(bell)
        if len(self.bells) > self.size:
            self.bells.pop(0)


class TypedBellTower(BellTower):
    def __init__(self, *args, bell_type=LittleBell):
        super().__init__(*[b for b in args if isinstance(b, bell_type)])
        self.bell_type = bell_type

    def append(self, bell):
        if isinstance(bell, self.bell_type):
            super().append(bell)