import re
with open("input.txt", "r", encoding="utf-8") as f:
    swords = {
        "narrative": set(),
        "question": set(),
        "exclamation": set()
    }
    for sentence in re.split(r'(?<=[.!?])\s*', f.read().strip()):
        if not sentence.strip():
            continue
        words = sentence[:-1].lower().split()
        if sentence[-1] == '.':
            swords["narrative"].update(words)
        elif sentence[-1] == '?':
            swords["question"].update(words)
        elif sentence[-1] == '!':
            swords["exclamation"].update(words)
    result_words = (swords["narrative"] & swords["question"]) - swords["exclamation"]
    print(' '.join(sorted(result_words)))