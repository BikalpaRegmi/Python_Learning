################################ Aggregating Functions #######################################


import numpy as np;

# WAP to perform aggregating functions.
a=np.array([1,3,5,6,2,4,1,2,11,39]);

print("Sum: ",np.sum(a));
print("Minimum: ",np.min(a));
print("Maximum: ",np.max(a));
print("Size: ",np.size(a));
print("Mean: ",np.mean(a));
print("Cumulative Sum: ",np.cumsum(a));
print("Cumulative Product: ",np.cumprod(a));


print("\n","\n");


# WAP to perform aggregating functions on price and quantiy two dimension arrays.
price = np.array([99,199,299,349,280]);
quantity = np.array([9,5,2,4,8]);

print("Price: ",price, "\n", "Quantity: ",quantity);

cp= np.cumprod([price,quantity],axis=0);
print("Product of two array: ", cp[1]);
print("Sum of price to pay: ", cp[1].sum());