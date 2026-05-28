import argparse


def print_error(text):
    print(f"ERROR: {text}!!")


if __name__ == "__main__":
    print('Welcome to my program')
    parser = argparse.ArgumentParser()
    parser.add_argument('error', nargs='*', type=str)
    args = parser.parse_args()
    print_error(" ".join(args.error))