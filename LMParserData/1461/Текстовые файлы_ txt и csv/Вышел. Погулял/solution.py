with open("poem.txt", "r", encoding="utf-8") as f:
    poem = f.read().strip().splitlines()

counting = ""
for i, stroka in enumerate(poem):
    counting += f"{i + 1} - {stroka}\n"

with open("counting.txt", "w", encoding="utf-8") as f:
    f.write(counting.strip())