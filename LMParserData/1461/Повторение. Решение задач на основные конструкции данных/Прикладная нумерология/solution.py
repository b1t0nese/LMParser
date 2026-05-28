hours = sorted(input().split(), key=int)
minutes = sorted(input().split(), key=int)

for hour in hours:
    for minute in minutes:
        if int(hour) <= 9:
            hour = f"0{int(hour)}"
        if int(minute) <= 9:
            minute = f"0{int(minute)}"
        if int(hour[0]) + int(hour[1]) != int(minute[0]) + int(minute[1]):
            print(f"{hour}:{minute}")