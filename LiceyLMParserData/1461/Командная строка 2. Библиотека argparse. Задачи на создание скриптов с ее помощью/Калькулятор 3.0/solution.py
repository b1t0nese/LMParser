import argparse
import sys

arg_count = len(sys.argv) - 1
if arg_count != 2:
    if arg_count == 0:
        print("NO PARAMS")
    elif arg_count == 1:
        print("TOO FEW PARAMS")
    elif arg_count > 2:
        print("TOO MANY PARAMS")
    exit()

parser = argparse.ArgumentParser()
parser.add_argument('a', type=str, nargs='?')
parser.add_argument('b', type=str, nargs='?')
args = parser.parse_args()

try:
    print(int(args.a) + int(args.b))
except Exception as e:
    print(e.__class__.__name__)