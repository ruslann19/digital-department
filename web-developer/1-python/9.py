import datetime

date_str = input()

date = datetime.datetime.strptime(date_str, "%d-%m-%Y")

weekday = date.weekday()

monday = date - datetime.timedelta(days=weekday)

monday_str = datetime.datetime.strftime(monday, "%d-%m-%Y")

print(monday_str)
