""" Question 1: Basic string manipulation using methods
Problem:
Write a Python program that:
-Takes a string from the user
-Converts it to uppercase
-Counts how many times the letter 'a' appears (case-insensitive)
-Replaces all spaces with hyphens (-) """

text=input("Plz enter a string: ");

print("upperCase", text.upper());
print("Number of a", text.lower().count('a'));
print("Replacing space with hyphen: ", text.replace(" ","-"));


"""Question 2: Checking string content using built-in methods
Problem:
Write a Python program that:
-Takes a string as input
-Checks if it contains only alphabets
-Checks if it contains only digits
-Checks if it is alphanumeric"""

text=input("Plz enter a string: ");

print("Only Alphabet: ",text.isalpha());
print("Only Digit: ", text.isdigit());
print("Alpha Numeric: ", text.isalnum());