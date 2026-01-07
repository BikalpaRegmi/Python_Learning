############################## Mathematical Operations in array ####################################

import numpy as np ;

# Wap to perform additions,substraction,multiplication & division between two single dimention arrays.
arr1=np.array([6,7,8,9,10]);
arr2=np.array([1,2,3,4,5]);
print(np.add(arr1,arr2));
print(np.subtract(arr1,arr2));
print(np.multiply(arr1,arr2));
print(np.divide(arr1,arr2));



# Wap to do power and square root of an array.
arr1=np.array([1,2,3,4]);
arr2=np.array([2]);
print("power: ",np.power(arr1,arr2));
print("squareRoot: ",np.sqrt(np.power(arr1,arr2)));



# Wap to perform additions,substraction,multiplication & division between two three dimention arrays.
arr1=np.array([[6,7],[8,8],[9,10]]);
arr2=np.array([[1,2],[3,3],[4,5]]);
print(np.add(arr1,arr2));
print(np.subtract(arr1,arr2));
print(np.multiply(arr1,arr2));
print(np.divide(arr1,arr2));