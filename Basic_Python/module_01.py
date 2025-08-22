# Write code below 💖

import random

symbols=['🍒','🍇', '🍉', '7️⃣']
results=random.choices(symbols, k=3)
output=("|".join(results))
print(output)
if output=="7️⃣|7️⃣|7️⃣":
  print("Jackpot!💰")
else:
  print("Thanks for playing")