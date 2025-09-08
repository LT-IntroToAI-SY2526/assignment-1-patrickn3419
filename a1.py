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
experience with [mention your previous programming language if any, or say 'I'm 
new to programming']. Can you create 5-7 practice problems that cover:

Variables and basic data types
Conditionals (if/elif/else)
Loops (for and while)
Functions
Basic list operations
Make them progressively more challenging. Make sure each problem has clear 
instructions and example inputs/outputs."

Example: "I'm learning Python basics in a high school programming class. 
I have some experience with Java. Can you create 5-7 practice problems that 
cover..."
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
    password_checker("wrongpassowrd") should return "Access denied"
    password_checker("") should return "You must enter a password."
  """
  if password == "admin123":
      return "Access granted!"
  elif password == "":
      return "You must enter a password."
  else:
      return "Access denied."


"""
PROBLEM 4: Countdown with a While Loop
Problem: Ask the user to enter a positive number, and then count down to 0, printing each number.

Example inputs/outputs:
Input:
  Enter a number: 5

Output:
  5
  4
  3
  2
  1
  0
"""


"""
PROBLEM 5: [Problem Title/Description]
[Copy the complete problem description from your AI assistant]

Example:
Problem: Write a function called 'is_even' that takes an integer and returns 
True if the number is even, False if it's odd.

Example inputs/outputs:
- is_even(4) should return True
- is_even(7) should return False
"""

"""
PROBLEM 6: [Problem Title/Description]
[Copy the complete problem description from your AI assistant]

Example:
Problem: Write a function called 'is_even' that takes an integer and returns 
True if the number is even, False if it's odd.

Example inputs/outputs:
- is_even(4) should return True
- is_even(7) should return False
"""

"""
PROBLEM 7: [Problem Title/Description]
[Copy the complete problem description from your AI assistant]

Example:
Problem: Write a function called 'is_even' that takes an integer and returns 
True if the number is even, False if it's odd.

Example inputs/outputs:
- is_even(4) should return True
- is_even(7) should return False
"""









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

print("\nTesting Problem 2:")
check_even_odd(32)

print("\nTesting Problem 3:")
# Add your tests here

print("\nTesting Problem 4:")
# Add your tests here

print("\nTesting Problem 5:")
# Add your tests here


