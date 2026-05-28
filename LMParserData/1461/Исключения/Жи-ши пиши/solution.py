rule_chars = (["ж", "ч", "щ", "ш"], ["ю", "ы", "я"])


class BrokenRuleError(Exception):
    pass


def check(text):
    for i in range(0, len(text)):
        if text[i].lower() in rule_chars[0] and text[i + 1].lower() in rule_chars[1]:
            raise BrokenRuleError("The rule is broken.")
    return "That's right."