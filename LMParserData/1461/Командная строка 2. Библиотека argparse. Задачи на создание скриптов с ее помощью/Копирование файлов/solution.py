import argparse

parser = argparse.ArgumentParser()
parser.add_argument("source_path", type=str)
parser.add_argument("destination_path", type=str)
parser.add_argument("--upper", action='store_true')
parser.add_argument("--lines", type=int, default=-1)
args = parser.parse_args()

with open(args.source_path, "r", encoding="utf-8") as f:
    file_data = f.read()

if args.lines >= 0:
    file_data = "\n".join(file_data.splitlines()[:args.lines])
if args.upper:
    file_data = file_data.upper()
if not file_data.endswith("\n"):
    file_data += "\n"

with open(args.destination_path, "w", encoding="utf-8") as f:
    f.write(file_data)