#################################################### SETS ######################################################


a={12,13,14,16,19,21,50,8,41};
b={11,15,17,19,23,27};
c={13,19,21,8};

# wap to find maximum and minimum in a set.
print("Minimum value: ",min(a));
print("Maximum value: ",max(a),);


# wap to find common element in three lists using sets.
print("Common element in all three: ",set(a)&set(b)&set(c));


# wap to find difference between two sets.
print("Difference between two sets: ", b.difference(a)); 


# wap to remove an item in a set if it is present in the set.
a.discard(50); 
a.discard(2); 
a.remove(12);
print(a);


# wap to check if the set is subset of another set.
print("Checks if a is subset of b: ",a.issubset(b));
print("Checks if c is subset of a: ",c.issubset(a));
