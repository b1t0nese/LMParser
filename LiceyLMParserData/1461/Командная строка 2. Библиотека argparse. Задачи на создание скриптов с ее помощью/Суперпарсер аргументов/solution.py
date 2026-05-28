import argparse

parser = argparse.ArgumentParser()
parser.add_argument('arg', nargs='*', default=None)
args = parser.parse_args()
print("\n".join(args.arg) if args.arg else "no args")