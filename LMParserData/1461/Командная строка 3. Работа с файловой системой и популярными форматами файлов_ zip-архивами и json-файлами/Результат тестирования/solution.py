import json

with open("scoring.json", "r") as f:
    scoring = json.load(f)["scoring"]
with open("input.txt", "r") as f:
    tests = iter(list(map(lambda x: x.strip(), f.read().splitlines())))

score = 0
for scor in scoring:
    one_test_score = scor["points"] // len(scor["required_tests"])
    for test in scor["required_tests"]:
        if next(tests) == "ok":
            score += one_test_score
print(score)