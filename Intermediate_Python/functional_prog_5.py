import random
from functools import reduce

prefixes = ['Mystic', 'Golden', 'Dark', 'Shadow', 'Silver']
suffixes = ['storm', 'song', 'fire', 'blade', 'whisper']

def capitalize_suffix(name):
    return name.capitalize()

# Use capped suffix list
capped_suffixes = list(map(capitalize_suffix, suffixes))

def create_fantasy_name(list_1, list_2):
    return random.choice(list_1) + ' ' + random.choice(list_2)

random_names = [create_fantasy_name(prefixes, capped_suffixes) for _ in range(10)]

def fire_in_name(name):
    return 'fire' in name.lower()

def concatenate_names(acc, name):
    return acc + ', ' + name if acc else name

filtered = list(filter(fire_in_name, random_names))
reduced = reduce(concatenate_names, filtered, "")

def display_name_info():
    for index, name in enumerate(random_names):
        print(f"name {index} - {name}")
    print("names with fire:", filtered)
    print("concatenated names in filtered:", reduced)

display_name_info()
