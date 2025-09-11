# Assignment 1: AI-Generated Python Problems
# Name: Patrick

"""
AI-Generated Problem Set

INSTRUCTIONS:
1. Document your original AI prompt below
2. Copy the problems your AI assistant generated
3. Implement solutions for each problem
4. Include comments explaining your approach
5. Test your solutions with different inputs

Remember: The goal is to LEARN, not just get working code!
"""

# =============================================================================
# PART 1: DOCUMENT YOUR AI COLLABORATION
# =============================================================================

"""
MY ORIGINAL AI PROMPT:
"I'm learning Python basics in a high school programming class. I have some 
experience with HTML, Javascript, and CSS from a taking a beginner level 
Web Development course. Can you create 5-7 practice problems that cover:

Variables and basic data types
Conditionals (if/elif/else)
Loops (for and while)
Functions
Basic list operations
Make them progressively more challenging. Make sure each problem has clear 
instructions and example inputs/outputs."
"""

# =============================================================================
# PART 2: AI-GENERATED PROBLEMS & SOLUTIONS
# =============================================================================

#Problem 1
def favorite_color(name: str, color: str) -> str:
  """
  PROBLEM 1: Warm-Up: Favorite Color

  Problem: Write a Python program that asks the user for their name and favorite color, then prints a sentence using both inputs.

  Example inputs/outputs:
  Input:
    favorite_color("Patrick", "red") should return "Hi Patrick! I heard your favorite color is red."
  """
  return f"Hi {name}! Your favorite color is {color}."

#Problem 2
def check_even_odd(number: int) -> str: # def declares a function(variable)
  """
  PROBLEM 2: Even or Odd Checker

  Problem: Write a function called check_even_odd(number) that: Takes one parameter: a number, and prints whether the number is even or odd

  Example inputs/outputs:
    check_even_odd(7) should return "7 is odd."
    check_even_odd(2) should return "2 is even."
  """
  if number % 2 == 0:
      return f"{number} is even."
  else:
      return f"{number} is odd."

#Problem 3
def password_checker(password: str) -> str:
  """
  PROBLEM 3: Password Checker
  Problem: Write a program that checks a user-entered password

  Example inputs/outputs:
    password_checker("admin123") should return "Access granted!"
    password_checker("wrongpassowrd") should return "Access denied."
    password_checker("") should return "You must enter a password."
  """
  if password == "admin123":
      return "Access granted!"
  elif password == "":
      return "You must enter a password."
  else:
      return "Access denied."

#Problem 4
def countdown(n: int) -> list[int]:
  """
  PROBLEM 4: Countdown with a While Loop
  Problem: Write a function that takes a positive number and returns a list counting down to 0.

  Example inputs/outputs:
    print(countdown(5)) should return [5, 4, 3, 2, 1, 0]
  """
  result = []
  while n >= 0:
    result.append(n)
    n -= 1
  return result

#Problem 5
def sum_to_n(n: int) -> int:
  """
  PROBLEM 5: Sum of First N Numbers
  Problem: Write a function that returns the sum of numbers from 1 to n.

  Example inputs/outputs:
    print(sum_to_n(5)) should return 15
  """
  total = 0
  for i in range(1, n+1):
    total += i
  return total

#Problem 6
def find_max(lst: list[int]) -> int:
  """
  PROBLEM 6: Find the Max in a List
  Problem: Write a function that returns the largest number in a list.

  Example inputs/outputs:
    print(find_max([3, 7, 2, 9, 4])) should return 9
  """
  if not lst:
     return None
  maxnum = lst[0]
  for num in lst[1:]:
      if num > maxnum:
        maxnum = num
  return maxnum

#Problem 7
def filter_even(lst: list[int]) -> list[int]:
  """
  PROBLEM 7: Filter Even Numbers
  Problem: Write a function that returns a new list of only the even numbers from a given list.

  Example inputs/outputs:
    print(filter_even([1, 2, 3, 4, 5, 6])) should return [2, 4, 6]
  """
  evens = []
  for num in lst:
    if num % 2 == 0:
        evens.append(num)
  return evens









# =============================================================================
# PART 3: TESTING YOUR SOLUTIONS
# =============================================================================


"""
Test all your solutions with different inputs

Add asserts if you feel comfortable

Example:
print("Testing Problem 1:")
print(f"is_even(4): {is_even(4)}")  # Should print True
print(f"is_even(7): {is_even(7)}")  # Should print False
"""

print("Testing Problem 1:")
# Add your tests here
print(favorite_color("Patrick", "red"))

print("\nTesting Problem 2:")
# Add your tests here
print(check_even_odd(32))
print(check_even_odd(981))

print("\nTesting Problem 3:")
# Add your tests here
print(password_checker("admin123"))
print(password_checker("wrongpassowrd"))
print(password_checker(""))

print("\nTesting Problem 4:")
print(countdown(5))
print(countdown(32))
# Add your tests here

print("\nTesting Problem 5:")
# Add your tests here
print(sum_to_n(5))
print(sum_to_n(32))

print("\nTesting Problem 6:")
# Add your tests here
print(find_max([3, 7, 2, 9, 4]))
print(find_max([12, 43, 1222, 5, 13985]))

print("\nTesting Problem 7:")
# Add your tests here
print(filter_even([12, 43, 51, 1, 3423, 55, 1, 3, 2]))
print(filter_even([1, 2, 3, 4, 5, 6]))


