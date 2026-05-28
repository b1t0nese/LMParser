import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--barbie', default=50, type=int)
parser.add_argument('--cars', default=50, type=int)
parser.add_argument('--movie', default="other", type=str)
args = parser.parse_args()

barbie = args.barbie if 0 <= args.barbie <= 100 else 50
cars = args.cars if 0 <= args.cars <= 100 else 50
movie = {
    "melodrama": 0,
    "football": 100,
    "other": 50
}.get(args.movie, 50)
boy = (100 - barbie + cars + movie) // 3
print(f"boy: {boy}\ngirl: {100 - boy}")