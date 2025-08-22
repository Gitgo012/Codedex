# Instance Methods
# Now that we can create classes and objects, and edit their properties, our last step is to create functions.

# Wait... functions in classes?! Isn't that super complicated?

# Actually, it's not. Functions that are defined in a class are called methods. In fact, we have already used a bunch of methods. For example, in exercise 25, we looked at a few built-in list methods, such as:

# .insert()
# .append()
# .remove()
# These are built-in methods. Let's create our own methods within a class!

# Consider our Student class:
class Student: 
  def __init__(self, name, year, enrolled, gpa):
    self.name = name
    self.year = year
    self.enrolled = enrolled
    self.gpa = gpa
  
  def display_info(self):
    print('The student ' + self.name + '\'s is ' + str(self.gpa) + '!')
  
  def graduation(self):
    if self.enrolled and self.gpa > 2.5 and self.year == 12:
      print(self.name + ' will be able to graduate this year!')
      
mitsuha = Student('宮水三葉', 11, False, 4.0)
taki = Student('立花瀧', 12, True, 4.8)

mitsuha.display_info()
taki.display_info()
mitsuha.graduation()
taki.graduation()

# It's time to open up a bank account! 🏦

# Create a file called bank_accounts.py.

# Let's define a BankAccount class. Then, let's use the __init__() method to set the following attributes:

# first_name (string)
# last_name (string)
# account_id (integer)
# account_type (string)
# pin (integer)
# balance (float)
# Next, let's create three methods:

# .deposit(): Add money into the account and return the new balance.
# .withdraw(): Take money out by subtracting from balance and returning the withdrawn amount.
# .display_balance(): Print the current value of balance.
# Lastly, initialize a new object from the BankAccount class and use these methods to do the following:

# Deposit $96 into the account.
# Withdraw $25 from the account.
# Print the current account balance.

class BankAccount():
    def __init__(self, first_name, last_name, account_id, account_type, pin, balance):
        self.first_name=first_name
        self.last_name=last_name
        self.account_id=account_id
        self.account_type=account_type
        self.pin=pin
        self.balance=balance
        
    def deposit(self, money):
        self.balance=self.balance+money
        return "Current balance is after deposit is",self.balance
    
    def withdraw(self,money):
        self.balance=self.balance-money
        if self.balance>0:
            return "balance after withdrawal is: ",self.balance
        else:
            return "Insufficient balance"
        
    def display_balance(self):
        return "balance is : ",self.balance
    
axisAccount=BankAccount("yash","kuletha",123434,"savings",1234,10)

print(axisAccount.deposit(96))
print(axisAccount.withdraw(25))
print(axisAccount.display_balance())
