import argparse


def count_lines(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return len(f.read().splitlines())
    except Exception:
        return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', type=str)
    args = parser.parse_args()
    print(count_lines(args.file))