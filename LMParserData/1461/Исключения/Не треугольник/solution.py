class NotEnoughError(Exception):
    pass


class DoNotMatchError(Exception):
    pass


def istriangle(*data):
    if len(data) != 3:
        raise NotEnoughError("Not enough arguments.")
    for coor in data:
        if len(coor) != 2:
            raise DoNotMatchError("The number of coordinates does not match.")
    return (
        data[0][0] * (data[1][1] - data[2][1])
        + data[1][0] * (data[2][1] - data[0][1])
        + data[2][0] * (data[0][1] - data[1][1])
    ) != 0