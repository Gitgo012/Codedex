# 💿 Theme: Indie Travel Songs

# for-in
# The first way is using a for-in loop. Here's an example:

snowfall = [0.3, 0.0, 0.0, 1.2, 3.9, 2.2, 0.8]

for i in snowfall:
  print(i)
  
# for-in with range() and len()
# We can also loop through a list using the index (position). To do so, we need the range() function and the len() function.

# As a reminder:

# range() function returns a sequence of numbers, from 0 to a number.
# len() function returns the length of the list.

snowfall = [0.3, 0.0, 0.0, 1.2, 3.9, 2.2, 0.8]

for i in range(len(snowfall)):
  print(snowfall[i])
  
# The i here is an index. This is saying for every index from 0 to the length of snowfall minus 1 (7 - 1 = 6), print out the item at that index.

playlist = [
  'Porches - rangerover',
  'Mount Eerie - You Swan, Go On',
  'Carolyn Polachek - Look at Me Now',
  'Pinegrove - Darkness',
  'LVL UP - Spirit Was',
  'Mitski - First Love / Late Spring'
]
# Now loop over the list and print everything out! 📻
for i in range(len(playlist)):
    print(f"Song {i} : {playlist[i]}")