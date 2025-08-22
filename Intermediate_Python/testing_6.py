# # Testing Object-Oriented Code
# Now for the moment you've been waiting for, let's learn to test object-oriented code focusing on classes and their methods.

# But first, a quick refresh. Object oriented code refers to code that uses objects and classes to leverage functionality.

# We want to make sure that our class objects and their methods work correctly under different conditions. This part of unit testing is unique as it involves verifying the behavior of classes and their interactions, rather than testing individual functions or procedures.

# ## setUp()
# Before we learn how to test class objects, let's explore two special methods.

# The setUp() method takes place before each test method is run. This ensures that each test method starts with a consistent state.

# For example, if we were testing a Person class object:

# class TestPerson(unittest.TestCase):
#   def setUp(self):
#     self.person = Person(name='Eddie', age=23)

# The setUp() method initializes a Person object (self.person) before each test method is executed.

# ## tearDown()
# Conversely, the tearDown() method happens after each test is run. It cleans up any resources leftover after testing. This could include:

# Closing a file object with .close().
# Deleting a class object from the global score via del.
# This method ensures that any changes made during testing are properly reverted and the environment is left in a clean state for the next test and can be run independently and consistently.

class BankAccount:
  def __init__(self, initial_balance=0):
    self.balance = initial_balance

  def deposit(self, amount):
    if amount <= 0:
      raise ValueError('Deposit amount must be positive')
    self.balance += amount
    return self.balance

  def withdraw(self, amount):
    if amount <= 0:
      raise ValueError('Withdrawal amount must be positive')
    if amount > self.balance:
      raise ValueError('Insufficient funds')
    self.balance -= amount
    return self.balance
        
initial_balance=BankAccount(100)

