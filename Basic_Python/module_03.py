import datetime, module_02
from module_02 import random_message
today=datetime.date.today()
# next_birthday=datetime.date(2026,4,1)
next_birthday=datetime.date(2025,8,21)

days_away=next_birthday-today
if today==next_birthday:
    print(random_message)
else:
    print(F"My next birthday is {days_away.days} days away!")