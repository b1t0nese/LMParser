def check_type(var):
    try:
        assert var + 0 == var
        try:
            assert var == int(var)
            return "int"
        except Exception:
            return "float"
    except Exception:
        try:
            assert var.upper() is not None
            return "str"
        except Exception:
            return "unknown"


class NoSubstringError(Exception):
    pass


def chirp(*data, **named_data):
    if "taboo" not in named_data.keys():
        raise NoSubstringError("No named argument.")
    new_data = []
    for dat in data:
        if check_type(dat) != "str":
            raise TypeError("The argument is not a string.")
        if named_data["taboo"] not in dat:
            new_data.append(dat)
    return sorted(new_data)