import sys
try:
    print(sum(map(lambda x: int(f"{"-" if x[0] % 2 != 0 else ""}{x[1]}"),
                  enumerate(sys.argv[1:]))) if len(sys.argv) > 1 else 'NO PARAMS')
except Exception as e:
    print(e.__class__.__name__)