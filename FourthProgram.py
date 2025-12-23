# To get Fibonacci series up to 15 numbers
a = 0
b = 1

print(a, end=" ");  # 0 (1st term)
print(b, end=" ");  # 1 (2nd term)

for i in range(1, 14):  
    c = a + b
    print(c, end=" ");
    a = b
    b = c



# To check if the number is prime or not.
num = int(input("Plz enter any one number: "));
if(num==1 or num==0):
    print("the number is neither prime nor composite.");
else:
    count=0;
    for i in range(2,num+1):
        if(num%i==0):
            count+=1;
    if(count==1):
        print("the number is prime.");
    else:
        print("the number is composite.");



# To find the reverse of the integer.
num=int(input("Plz enter a int number: "));
rev=0;
while(num>0):
   temp=num%10;
   rev=rev*10+temp;
   num=num//10;
print("Reverse of yout input is: ",rev);


