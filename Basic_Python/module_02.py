# The datetime module specializes in dates and times. Just like random, it comes with Python by default and can simply be imported.

# In addition to functions, modules may contain class object definitions with their own defined methods and properties.

# The datetime module has a date object that accepts the following properties:

# .year: An integer between 1 and 9999.
# .month: An integer between 1 and 12.
# .day: An integer between 1 and the number of days in a given month.
# The syntax for a date is datetime.date(year, month, day), like so:

import datetime
import random
release_date = datetime.date(1991, 2, 20)
# print(release_date)     # Output: 1991-02-20

# print(f'Python was released in {release_date.year}.')

#to get the current date 
# print(datetime.date.today())

birthday_wishes = [
    "Hope you have a very Happy Birthday! 🎈",
    "It's your special day – get out there and celebrate! 🎉",
    "You were born and the world got better – everybody wins! 🥳",
    "Have lots of fun on your special day! 🎂",
    "Another year of you going around the sun! 🌞"
]

random_message=random.choice(birthday_wishes)
