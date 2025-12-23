# To find the sum of all the even numbers upto 50.
sum=0;

for i in range (1,51) :
 if(i%2==0) :
  sum+=i;
 
print("SUM of first 50 even int is :", sum );



# To write first 20 numbers and thier square numbers.
for i in range (1,20) :
  print(i, "Square= ",i*i );


# To find sum of first 10 odd numbers using while loop.
sum=0;
n=0;

while n<=20 :
  if(n%2!=0) :
    sum+=n;
  n+=1;
print("Sum of first 10 odd number is: ", sum );    


# To check if a number is divisible by 8 or 12 upto 100 numbers.
n=0;
exist=0;

enter=int(input("Plz enter a number: "));

while (n<=100) :
  if(enter%8==0 or enter%12==0) :
    exist=1;
  n+=1;

if(exist==1) :
  print("The number is divisible by either 12 or 8." ,"\n");
else :
  print("The number is not divisible by neither 12 nor 8." ,"\n");


# To create a billing system at SuperMarket.
while True:
  name=input("Enter the name of the customer: ");
  total=0;
 
  while True:
    print("Plz enter the amount and quantity.");
    amt=float(input("Enter price of that item: "));
    qnt=float(input("Enter quantity of that item: "));
    total+=amt*qnt;
    repeat=input("Do you wanna add more items ? (y/n)");
    if(repeat=="n" or repeat=="N"):
      break;
  print("-" *40);
  print("Name: " ,name);
  print("Amount to be paid: ",total);
  print("-" *40);
  print("**********Happy Shopping************");

  repeat1=input("Do you wanna add more customers ? (y/n)");
  if(repeat1=="n" or repeat1=="N"):
   break;