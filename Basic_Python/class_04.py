# Since 1996, the Pokémon video game franchise has delighted players around the world with collectible pocket monsters. A Pokédex is a device that tracks the information for Pokémon that are seen or caught.

# Create a new file called pokedex.py.

# Next, let's define a Pokemon class with the following attributes:

# entry (integer)
# name (string)
# types (list of strings)
# description (string)
# is_caught (boolean)
# Note: Make sure to use the __init__() method.

# Next, create an instance method called .speak() that prints a string of the sound a Pokémon makes. A Pokémon usually just says their name, so make the .speak() simply print out their name twice!

# Then, create another instance method called .display_details() that prints the attributes of a Pokemon object like the following:

class Pokemon:
    def __init__(self, entry, name, types, description, is_caught):
        self.entry=entry
        self.name=name
        self.types=types
        self.description=description
        self.is_caught=is_caught
        
    def display_details(self):
        return (f"Entry number: {self.entry}\n Name: {self.name}\n Type: {self.types} Description: {self.description}")
    
    def speak(self):
        return (f"{self.name} {self.name}!")
    
# Create 3 instances
pikachu = Pokemon(25, "Pikachu", "Electric", "A Mouse Pokémon. It keeps its tail raised to monitor its surroundings.", True)
charmander = Pokemon(4, "Charmander", "Fire", "Obviously prefers hot places. When it rains, steam is said to spout from the tip of its tail.", False)
bulbasaur = Pokemon(1, "Bulbasaur", "Grass/Poison", "A strange seed was planted on its back at birth. The plant sprouts and grows with this Pokémon.", True)

# Use both methods
print(pikachu.display_details())
print(pikachu.speak())
print("--------------")
print(charmander.display_details())
print(charmander.speak())
print("--------------")
print(bulbasaur.display_details())
print(bulbasaur.speak())
