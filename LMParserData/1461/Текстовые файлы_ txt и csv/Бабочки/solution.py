butt_files = input().split("; ")
butters = []
for butt_file in butt_files:
    with open(butt_file, "r", encoding="utf-8") as f:
        butters.append(f.read().splitlines())

gotchas_butts = []
for i, butts in enumerate(butters):
    for butt in butts:
        gotcha = 1
        for j, other_butts in enumerate(butters):
            if butt in other_butts and j != i:
                gotcha += 1
        if gotcha == 2 and butt not in gotchas_butts:
            gotchas_butts.append(butt)

print("\n".join(gotchas_butts))