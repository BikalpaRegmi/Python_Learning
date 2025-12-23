
# To check if a number is positive,negative or zero.
print("***Positive/Negative CALCULATOR***");
num = int(input("plz enter a number "));
if(num>0):print("positive");
elif(num<0):print("Negative");
else:print("Zero");



# To check if a number is odd or even.
print("***Odd/Even CALCULATOR***");
num=int(input("plz enter an number "));
if(num%2==0):print("even");
else:print("odd");


# To calculate area user choosed diagram.
print("***AREA CALCULATOR***");
print("Press 1 for area of rectangle \n Press 2 for area of square");
choose=int(input("Plz enter an number u wanna choose: "));
if(choose==1):
    l=int(input("Plz enter a length: "));
    b=int(input("plz enter breadth: "));
    print("Area of rectangle is: ", l*b);

else: 
 l=int(input("Plz enter a length: "));
print("Area of square is: ",l*l);

# To calculate if the passed letter is vowel or consonant
print("***Vowel/Consonant CALCULATOR***");
letter = input("Plz enter a letter: ");
if letter in "aeiou": print("The letter is Vowel");
else: print("the letter is consonant");


#To print the number of digit entered.
print("***DIGIT NUMBER***");
num = int(input("Plz enter a number: "));
if(num>=0 and num<10):print("number has 1 digit");
elif(num>=10 and num<100):print("number has 2 digit");
elif(num>=100 and num<1000):print("number has 3 digit");
elif(num>=1000 and num<10000):print("number has 4 digit");
elif(num>=10000 and num<100000):print("number has 5 digit");