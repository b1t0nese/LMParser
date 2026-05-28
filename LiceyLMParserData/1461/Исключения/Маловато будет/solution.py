word = ""
for i in range(6):
    try:
        line = input()
        word += line[(len(line) - 1) // 2]
    except Exception:
        break
try:
    assert len(word) == 6, f"Error EOF, {len(word)} of lines entered."
    print(word)
except Exception as e:
    print(e)