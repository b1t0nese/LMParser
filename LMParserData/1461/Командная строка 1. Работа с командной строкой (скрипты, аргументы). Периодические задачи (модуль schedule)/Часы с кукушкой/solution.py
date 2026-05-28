import datetime
import schedule
import sys

output_type = (len(sys.argv) > 1 and sys.argv[1]) or "lines"
# "lines" (выводить h строк) или "stings" (выводить h слов в 1 строку)
# в условии как-будто нужен всё же первый вариант
# если нужно изменить, можно написать: python main.py strings


def job():
    time = datetime.datetime.now()
    hour, min = int(time.hour), int(time.minute)
    if min == 0:
        kucount = 12 if hour == 12 else hour % 12
        if output_type == "lines":
            list(map(lambda x: print("Ку"), range(kucount)))
        elif output_type == "strings":
            print(str("Ку " * kucount).strip())


schedule.every().minute.do(job)
while True:
    schedule.run_pending()