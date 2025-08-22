# Write code below 💖
#Here is how we write list comprehensions in Python:
#[expression for item in dataset if condition]
#example
# Original approach using a loop
# numbers = [1, 2, 3, 4, 5]
# squares = []
# for num in numbers:
#   squares.append(num ** 2)

# # Using a list comprehension to square each number
# squared_numbers = [num ** 2 for num in numbers]

# # Displaying the outcomes
# print('Original Numbers:', numbers)
# print('Squared Numbers:', squared_numbers)
numbers = [57, 10, 82, 36, 89, 46, 13, 23, 92, 48]
def even(numbers):
  even_num= [num for num in numbers if num%2==0]
  return even_num

print("even numbers", even(numbers))
print("original numbers", numbers)
