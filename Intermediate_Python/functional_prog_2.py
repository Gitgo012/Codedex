# Write code below 💖

#In functional programming, higher-order functions can take other functions as arguments or return functions as results. Like Swiss Army knives, higher-order functions are versatile and efficient. They enable us to create powerful and reusable Python code.

#example
# Define the Higher-order function 
# def apply_operation(operation, numbers):
#   result = []
#   for num in numbers:
#     result.append(operation(num))
#   return result

# # Example operation
# def double(x):
#   return x * 2

# # List of numbers
# numbers_list = [1, 2, 3, 4, 5]

# # Using the higher-order function
# doubled_numbers = apply_operation(double, numbers_list)

# # Displaying the outcomes
# print('Original Numbers:', numbers_list)
# print('Doubled Numbers:', doubled_numbers)

def translator(language):
  translations = {
  'spanish': {'hello': 'hola', 'goodbye': 'adiós', 'thank you': 'gracias'},
  'french': {'hello': 'bonjour', 'goodbye': 'au revoir', 'thank you': 'merci'},
  'italian': {'hello': 'ciao', 'goodbye': 'arrivederci', 'thank you': 'grazie'}
  }

  def translate_word(word):
    if word.lower() in translations[language]:
      return translations[language][word]
    else:
      return "Translation not available"
  return translate_word

#usage
translate_to_spanish = translator('spanish')
print(translate_to_spanish('hello')) # Output: hola

translate_to_french = translator('french')
print(translate_to_french('hello'))  # Output: bonjour

translate_to_italian = translator('italian')
print(translate_to_italian('hello'))  # Output: ciao

translate_to_italian = translator('italian')
print(translate_to_italian('tonight'))  # Output: Translation not available