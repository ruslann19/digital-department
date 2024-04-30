import datetime
import math

def gift_count(budget, month, birthdays):
    birthdays_in_month = []
    for key, value in birthdays.items():
        if value.month == month:
            birthdays_in_month.append((key, value))

    count = len(birthdays_in_month)
    res = ""
    if count == 0:
        res += "В этом месяце нет именинников."
    else:
        birthdays_in_month = sorted(birthdays_in_month, key=lambda item: item[1].day)

        res += f"Именинники в месяце {month}: "
        for key, value in birthdays_in_month:
            date_str = value.strftime("%d.%m.%Y")
            res += f"{key} ({date_str}), "
        
        res = res[:len(res) - 2] + ". "

        gift = math.floor(budget / count)
        res += f"При бюджете {budget} они получат по {gift} рублей."

    print(res)

# ----------------------------------------------------------------

# birthdays = {"Иванов Иван Иванович": datetime.date(1989, 5, 1), "Петров Петр Петрович": datetime.date(1998, 5, 6)}

# gift_count(20000, 5, birthdays)

# birthdays = {"Катя": datetime.date(1989, 1, 1), "Ваня": datetime.date(1971, 1, 5)}

# gift_count(20000, 1, birthdays)
