from datetime import date

dateNOW = str(date.today())

print(f"Початкова дата: {dateNOW}")

year = dateNOW[0:4]

month = dateNOW[5:-3]

day = dateNOW[8:]

print("Відповідь: {0}/{1}/{2}".format(day, month, year))
