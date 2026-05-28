import sys
output = []
sort = False
for arg in sys.argv[1:]:
    if arg == "--sort":
        sort = True
    if "=" in arg:
        output.append(arg.split("="))
output = sorted(output) if sort else output
for obj in output:
    print("Key:", obj[0], "Value:", obj[1])