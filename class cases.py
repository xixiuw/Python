#Here are some progressive exercises for learning classes in Python, from basic to more complex:

### 1. Basic Class - Pet

# Create a simple Pet class with basic attributes and methods
class Pet:
    def __init__(self, name, animal_type, age):
        self.name = name
        self.animal_type = animal_type
        self.age = age
    
    def get_info(self):
        return f"{self.name} is a {self.animal_type} and is {self.age} years old"

# Test it
my_pet = Pet("Buddy", "dog", 5)
print(my_pet.get_info())

### 2. Rectangle Class with Calculations

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)
    
    def is_square(self):
        return self.length == self.width

# Test it
rect = Rectangle(5, 3)
print(f"Area: {rect.area()}")
print(f"Perimeter: {rect.perimeter()}")
print(f"Is square? {rect.is_square()}")


### 3. Student Class with Grade Management

class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []
    
    def add_grade(self, grade):
        if 0 <= grade <= 100:
            self.grades.append(grade)
            return True
        return False
    
    def get_average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)
    
    def get_highest_grade(self):
        if not self.grades:
            return None
        return max(self.grades)

# Test it
student = Student("Alice")
student.add_grade(85)
student.add_grade(92)
student.add_grade(78)
print(f"Average: {student.get_average():.2f}")
print(f"Highest grade: {student.get_highest_grade()}")


### 4. Bank Account with Transaction History

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.transactions = []
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposit: +${amount}")
            return True
        return False
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrawal: -${amount}")
            return True
        return False
    
    def get_transaction_history(self):
        return self.transactions
    
    def get_balance(self):
        return f"Current balance: ${self.balance}"

# Test it
account = BankAccount("John Doe", 100)
account.deposit(50)
account.withdraw(30)
print(account.get_balance())
print("Transaction history:")
for transaction in account.get_transaction_history():
    print(transaction)

### 5. Library Book Management System

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_checked_out = False
        self.borrower = None

    def check_out(self, borrower_name):
        if not self.is_checked_out:
            self.is_checked_out = True
            self.borrower = borrower_name
            return True
        return False

    def return_book(self):
        if self.is_checked_out:
            self.is_checked_out = False
            self.borrower = None
            return True
        return False

class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)
    
    def find_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None
    
    def list_available_books(self):
        return [book.title for book in self.books if not book.is_checked_out]

# Test it
library = Library()
library.add_book("The Hobbit", "J.R.R. Tolkien")
library.add_book("1984", "George Orwell")

book = library.find_book("The Hobbit")
if book:
    book.check_out("Alice")
    print(f"Available books: {library.list_available_books()}")
    book.return_book()
    print(f"Available books after return: {library.list_available_books()}")


### Practice Exercises:
"""
1. Modify the Pet class to include:
   - A method to celebrate birthday (increase age)
   - A method to make sound based on animal type
   - A list of favorite toys

2. Enhance the Student class with:
   - A method to calculate letter grade
   - Support for different subjects
   - Grade point average calculation

3. Create a Car class with:
   - Fuel management
   - Mileage tracking
   - Maintenance schedule

4. Build a Shopping Cart class that:
   - Manages items and quantities
   - Calculates total price
   - Applies discounts
   - Handles inventory

Would you like me to:
1. Explain any of these examples in more detail?
2. Provide more exercises?
3. Show how to extend these classes further?
4. Demonstrate inheritance with these examples?
"""



#I'll demonstrate inheritance using some of our previous examples and create new ones to show different aspects of inheritance.

### 1. Pet Inheritance Hierarchy

class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def make_sound(self):
        return "Some generic pet sound"
    
    def get_info(self):
        return f"{self.name} is {self.age} years old"

class Dog(Pet):
    def __init__(self, name, age, breed):
        super().__init__(name, age)  # Call parent class's __init__
        self.breed = breed
    
    def make_sound(self):  # Override parent's method
        return "Woof!"
    
    def fetch(self):  # Dog-specific method
        return f"{self.name} is fetching the ball"

class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
    
    def make_sound(self):
        return "Meow!"
    
    def scratch(self):
        return f"{self.name} is scratching"

# Test it
dog = Dog("Buddy", 5, "Golden Retriever")
cat = Cat("Whiskers", 3, "Orange")

print(dog.get_info())  # Inherited from Pet
print(dog.make_sound())  # Overridden method
print(dog.fetch())  # Dog-specific method

print(cat.get_info())  # Inherited from Pet
print(cat.make_sound())  # Overridden method
print(cat.scratch())  # Cat-specific method


### 2. Bank Account Inheritance

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.transactions = []
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposit: +${amount}")
            return True
        return False
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrawal: -${amount}")
            return True
        return False

class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=0.01):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate
    
    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.deposit(interest)
        return f"Added ${interest:.2f} interest"

class CheckingAccount(BankAccount):
    def __init__(self, owner, balance=0, overdraft_limit=100):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit
    
    def withdraw(self, amount):  # Override withdraw to handle overdraft
        if amount > 0 and (self.balance - amount) >= -self.overdraft_limit:
            self.balance -= amount
            self.transactions.append(f"Withdrawal: -${amount}")
            return True
        return False

# Test them
savings = SavingsAccount("John Doe", 1000, 0.05)
checking = CheckingAccount("John Doe", 500, 200)

savings.deposit(500)
print(savings.add_interest())
print(f"Savings balance: ${savings.balance}")

checking.withdraw(600)  # This works due to overdraft
print(f"Checking balance: ${checking.balance}")


### 3. Shape Hierarchy with Abstract Class

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass
    
    def describe(self):
        return f"Area: {self.area():.2f}, Perimeter: {self.perimeter():.2f}"

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
    
    def describe(self):
        return f"Square with side {self.length}: " + super().describe()

# Test them
rect = Rectangle(5, 3)
circle = Circle(4)
square = Square(5)

print(rect.describe())
print(circle.describe())
print(square.describe())

"""
### Key Inheritance Concepts Demonstrated:
1. **Basic Inheritance**: Child classes inherit methods and attributes from parent class
2. **super()**: Used to call methods from parent class
3. **Method Overriding**: Child classes can modify parent class methods
4. **Abstract Classes**: Define a common interface for related classes
5. **Multiple Levels**: Inheritance can be multiple levels deep (like Square inheriting from Rectangle)

### Practice Exercises for Inheritance:
1. Add a `Bird` class to the Pet hierarchy that can fly
2. Create a `BusinessAccount` that inherits from `BankAccount`
3. Add a `Triangle` class to the Shape hierarchy
4. Create a `CreditAccount` that inherits from `BankAccount` with credit limit

Would you like me to:
1. Explain any of these concepts in more detail?
2. Show more examples of specific inheritance features?
3. Demonstrate multiple inheritance?
4. Show how to use inheritance with other Python features?
"""