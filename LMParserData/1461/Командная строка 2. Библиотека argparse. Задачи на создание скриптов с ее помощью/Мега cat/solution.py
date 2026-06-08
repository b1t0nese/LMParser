import argparse
import os


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type=str)
    parser.add_argument('--count', action='store_true')
    parser.add_argument('--num', action='store_true')
    parser.add_argument('--sort', action='store_true')
    args = parser.parse_args()
    
    if not os.path.exists(args.filename):
        print("ERROR")
        return
    
    try:
        with open(args.filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
    except Exception:
        print("ERROR")
        return
    
    lines = [line.rstrip('\n') for line in lines]
    
    if args.sort:
        lines.sort()
    
    if args.num:
        for i, line in enumerate(lines):
            print(f"{i} {line}")
    else:
        for line in lines:
            print(line)
    
    if args.count:
        print(f"rows count: {len(lines)}")


if __name__ == '__main__':
    main()