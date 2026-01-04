######################################## Functions ########################################


# Write a function to find maximum of three numbers in python.
def max(x,y,z):
    if(x>y and x>z):
        print("The maximum is ",x);
    elif(y>z and y>x):
        print("The maximum is ",y);
    else:
        print("The maximum is ",z);

a,b,c = map(int,input("Plz enter a number: ").split());
max(a,b,c);



# Write a function to create and print a list where the values are square of numbers between 1 and 30.
def square():
    list=[];
    for i in range(1,31):
        list.append(i**2);
    return list;
print(square());



# Write a function that takes a number as a parameter and check if the number is prime or not.
def checkPrime(x):
    if(x==1 or x==0):
        print("The ",x," is neither prime nor composite");
    count=0;
    for i in range (1,x+1):
        if(x%i==0):
            count+=1;
    return count;

num=int(input("Plz enter any one number: "));
if(checkPrime(num)==2):
    print("Prime");
else:
    print("Composite");



# Write a python function to sum all the numbers in a list.
def sumAll(numbers):
    total=0;
    for i in numbers:
        total+=i;
    return total;
lst=[];
n=int(input("Enter how many is your number of list items: "));
for i in range(0,n):
    value=int(input("Plz enter a value : "));
    lst.append(value);
print("Sum of all value inside list is: ",sumAll(lst));



# Write a python program to solve the fibonacci sequence using recursion.
def fibonacci(x):
    if(x==0):
        return 0;
    elif(x==1):
        return 1;
    else:
        return fibonacci(x-1)+fibonacci(x-2);

n=int(input("Enter any one value: "));
for i in range(0,n):
    print(fibonacci(i),end=" ");   
    