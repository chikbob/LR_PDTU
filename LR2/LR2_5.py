import re

i = 1

list_day = tuple(
    [
        "понеділок",
        "вівторок",
        "середа",
        "четверг",
        "п'ятниця",
        "субота",
        "неділя",
    ]
)

for day in tuple(list_day):
    if i <= 5:
        print(f"{i}-й день тижня - {day} робочий день")
    else:
        print(f"{i}-й день тижня - {day} вихідний день")
    i += 1
