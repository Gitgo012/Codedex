# Write code below 💖
#pure functions is a function whose output is derived solely from its input values without any side effects and it always returns the same result for same input
# def impure_squared(number):
#   result = number ** 2
#   print('The square of', number, 'is', result)
#   return result

# def pure_squared(number):
#   return number ** 2
#impure function prints something to the terminal also(side effect)
#pure function only returns the squared value of the number

def calculate_circle_area(radius):
  return 3.14*(radius**2)

#usage

rad=float(input("enter the radius of the circle in cm: "))
print(f"area: {calculate_circle_area(rad)} cm2")

# def main():
#     rad=float(input("enter the radius of the circle in cm: "))
#     print(f"area: {calculate_circle_area(rad)} cm2")
    
# if __name__=='__main__':
#     main()