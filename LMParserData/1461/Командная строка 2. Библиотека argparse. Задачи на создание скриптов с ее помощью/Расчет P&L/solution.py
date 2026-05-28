import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--per-day', type=int, default=0)
parser.add_argument('--per-week', type=int, default=0)
parser.add_argument('--per-month', type=int, default=0)
parser.add_argument('--per-year', type=int, default=0)
parser.add_argument('--get-by', type=str, choices=["day", "month", "year"], default="day")
args = parser.parse_args()

if args.get_by == "day":
    days = 1
elif args.get_by == "month":
    days = 30
elif args.get_by == "year":
    days = 360

output = 0
output += args.per_day * days
output += args.per_week * (days / 7)
output += args.per_month * (days / 30)
output += args.per_year * (days / 360)

print(int(output))