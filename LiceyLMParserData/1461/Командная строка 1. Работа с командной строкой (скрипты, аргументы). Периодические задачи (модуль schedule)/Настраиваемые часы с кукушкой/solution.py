import datetime
import schedule
import sys

ku_text = (len(sys.argv) > 1 and sys.argv[1]) or "Ку"
ku_diap = (len(sys.argv) > 2 and sys.argv[2]) or "00-24"
ku_diap = list(map(int, ku_diap.split("-")))


def job():
    time = datetime.datetime.now()
    hour, min = int(time.hour), int(time.minute)
    if min == 0 and ku_diap[0] <= hour <= ku_diap[1]:
        list(map(lambda x: print(ku_text), range(12 if hour == 12 else hour % 12)))


schedule.every().minute.do(job)
while True:
    schedule.run_pending()