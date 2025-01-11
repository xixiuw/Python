# Exercise 1: String Manipulation
name = input("What's your name? ")
age = input("How old are you? ")
print(f"In 10 years, {name} will be {int(age) + 10} years old")

# Exercise 2: Lists and Loops
numbers = [1, 2, 3, 4, 5]
sum = 0
for num in numbers:
    sum += num
print(f"Sum is: {sum}")

# Exercise 3: Functions
def is_even(number):
    return number % 2 == 0

# Test with different numbers
print(is_even(4))  # True
print(is_even(7))  # False