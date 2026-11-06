class SpeedLimitError(Exception):
    pass


class DataError(Exception):
    pass


def not_exceed(*data):
    result = []
    for d in data:
        if d.get('settlement') and d.get("limit") is not None and d.get("limit") > 60:
            raise SpeedLimitError("Speed limit controversy.")
        elif d.get('fine') == 0:
            raise DataError("Error in data.")
        base_limit = ((60 if d.get('settlement') else 90) if d.get("limit") is None else d.get("limit"))
        if d['speed'] > base_limit + d['delta']:
            result.append(d['fine'])
        else:
            result.append(0)
    return result