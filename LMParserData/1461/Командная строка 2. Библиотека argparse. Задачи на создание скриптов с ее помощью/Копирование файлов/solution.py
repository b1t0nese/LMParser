import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('source', type=str)
    parser.add_argument('destination', type=str)
    parser.add_argument('--upper', action='store_true')
    parser.add_argument('--lines', type=int)
    args = parser.parse_args()
    
    with open(args.source, 'r', encoding='utf-8') as source_file:
        lines = source_file.readlines()
    
    if args.lines is not None:
        lines = lines[:args.lines]
    
    if args.upper:
        lines = [line.upper() for line in lines]
    
    with open(args.destination, 'w', encoding='utf-8') as dest_file:
        dest_file.writelines(lines)