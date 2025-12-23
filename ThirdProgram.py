""" Question 1: Basic string manipulation using methods
Problem:
Write a Python program that:
-Takes a string from the user
-Converts it to uppercase
-Counts how many times the letter 'a' appears (case-insensitive)
-Replaces all spaces with hyphens (-) 
-Checks if it contains only alphabets
-Checks if it contains only digits
-Checks if it is alphanumeric
-reverse it
-Check if it is palindrome
-Check the number of vowels
-Check if every words starts with capital letter."""

text=input("Plz enter a string: ");

print("upperCase", text.upper());
print("Number of a", text.lower().count('a'));
print("Replacing space with hyphen: ", text.replace(" ","-"));
print("Only Alphabet: ",text.isalpha());
print("Only Digit: ", text.isdigit());
print("Alpha Numeric: ", text.isalnum());
print("Reverse: ", text[::-1]);
print("Palindrome: ", text[::-1]==text);
print("Capitalize: ",text.istitle());

vowel=0
for i in text.lower():
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
        vowel+=1;
print("Number of vowel: ",vowel);




# To seperate following string into coma(,) seprated value. {A="OOTD.YOLO.ASAP.BRB.GTG.OTW"}
A="OOTD.YOLO.ASAP.BRB.GTG.OTW";
print("Comma seperated: ", A.split("."));

# To sort strings alphabetically.
txt=input("Plz enter a string: ");
print("Sorted text: ", sorted(txt));

# To remove e characters and fullstop from a string. 
a="Hello world.";
print("Removed o: ", a.replace("o",""));
print("Removed .: ", a.replace(".",""));


