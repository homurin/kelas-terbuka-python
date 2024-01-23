import datetime as dt

today = dt.date.today()
print(f'today date is {today}')
print(f'today day is {today:%A}')

date = dt.date(2001, 11, 12)
print(f'My birth date is {date}')

day = 12
month = 11
year = 2001

birth_date = dt.date(year, month, day)
print(f'Your birth date is {birth_date}')
print(f'The day you birth is {birth_date:%A}')

day_passed = (today - birth_date)
current_age = day_passed // 365
reminder_month = (day_passed.days % 365) // 30

print(f'Your age is {current_age.days} year, {reminder_month} month')
