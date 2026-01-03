"""
Given, A=["Ross","Rachel","Monica","Joe"].
-To swap first and forth element.
-To add new value at last position.
-To add new value at second position.
-To delete the value from 3rd position.
"""
A=["Ross","Rachel","Monica","Joe"];
A[0],A[3] = A[3],A[0];
print("Swap: ",A);
A.append("Alice");
print("New Value at last: ",A);
A.insert(1,"Bob");
print("New Value at middle: ",A);
A.pop(2);
print("Delete Value at middle: ",A);


"""
Given, B=[13,7,12,10].
-To multiply all the numbers in the list.
-To get largest from the list.
-To get the smallest from the list.
"""
mul=1;
B=[13,7,12,10];
for i in B:
    mul*=i;
print("Total multiplication is: ",mul);
B.sort();
print("Largest value from the list: ", B[-1]);
print("Smallest value from the list: ", B[0]);


"""
Given, Y=[1,2,"Bob",False,2] Z=["Eden","Frank","George",True,19,2]
-Merge these two Lists into one single.
-Delete Bob,19 and False by value not position.
-Count how many times has 2 occured.
-Find the position of item where False lies.
-Remove all element.
"""
Y=[1,2,"Bob",False,2];
Z=["Eden","Frank","George",True,19,2];

Y.extend(Z);
print("Merged List: ",Y);

Y.remove("Bob");
Y.remove(19);
Y.remove(False);
print("Deleted List: ",Y);

print("Num of times 2 occured: ",Y.count(2));

Y.clear();
print("List after clear: ",Y);