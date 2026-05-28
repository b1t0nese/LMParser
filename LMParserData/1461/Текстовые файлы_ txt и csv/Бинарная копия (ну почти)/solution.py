with open("data.bin", "rb") as f1:
    data = f1.read()
    with open("part.dat", "wb") as f2:
        f2.write(data[:100])