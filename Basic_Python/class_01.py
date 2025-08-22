# Suppose we want to build a database of students in a school, where each student has different attributes, like name, year, GPA, and enrollment status.

# Using our previous knowledge, we could represent each student as a list:
# Lists with student id, name, year, gpa, and enrolled status

student_1 = [1001, 'Asiqur', 10, 3.7, True]
student_2 = [1002, 'Jerry', 9, 3.8, True]
student_3 = [1003, 'Rose', 12, 3.6, False]

# However, we have no way of knowing which item corresponds to which attribute – it will get messy fast. For example, does student_2[1] refer to the name, year, or GPA?

# This is where classes come in!

# With classes, we can create our own data types and use them to model everyday objects with unique characteristics and behaviors.

# Classes serve as a template for the objects created using that class. Simply put, a class is like a blueprint. It can make a bunch of objects with identical sets of attributes, similar to how a car manufacturer can use a model blueprint to build hundreds of cars with different colors, interiors, wheels, etc.
#basic syntax
# class Name:
  # Attributes inside
  
  
# The class keyword followed by class name creates the class. By convention, the class name is capitalized.

class Student:
  name = 'yash'
  year = 2022
  cgpa = 8.1
  enrolled = True
  
student_1=Student()
print(student_1.name)
print(student_1.year)
print(student_1.cgpa)
print(student_1.enrolled)

#restaurant class
class Restaurent:
    name=""
    category=""
    rating=0.0
    delivery=False
    
bobs_burger=Restaurent()
bobs_burger.name='Bob\'s Burgers'
bobs_burger.category='American Diner'
bobs_burger.rating=4.7
bobs_burger.delivery=False

#You can check all the attributes available on the bobs_burger object with the built-in vars() function, as follows:
print(vars(bobs_burger))
#output
# {'name': "Bob's Burgers", 'category': 'American Diner', 'rating': 4.7, 'delivery': False}
#one more instance
yash_diner=Restaurent()
yash_diner.name="Yash\'s Diner"
yash_diner.category='Diner'
yash_diner.rating=4.8
yash_diner.delivery=False

hariyali=Restaurent()
hariyali.name="Hariyali"
hariyali.category="Veg restaurant"
hariyali.rating=4.0
hariyali.delivery=True

print(vars(yash_diner))
print(vars(hariyali))