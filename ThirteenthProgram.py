############################## Sort, Filter & Search in Arrays ##################################

import numpy as np ;

# Wap to perform sort operation in python.
arr=np.array([18,12,19,14,13,16]);
print("Sorted Array: ",np.sort(arr));

arr1=np.array([[18,12,19],[15,17,11]]);
print("Sorted 2d Array: ",np.sort(arr1));



# Wap to perform search operation in python.
arr2=np.array([18,12,19,14,13,16]);
print("Index of 13 value: ",np.where(arr2 == 13))
print("Index of values that are divisible by 2: ",np.where(arr2 %2== 0))

sortedArr2 =np.sort(arr2);
ss=np.searchsorted(sortedArr2,19) 
print("Index of 19 value after sorting ",ss);

arr_2d=np.array([[18,12,19],[15,17,11]]);
print("Index of values in 2d divisible by 2: ",np.where(arr_2d%2==0));


# Wap to perform filter opertaion in python.
arr3=np.array([18,12,19,14,13,16]);
print("values less than 14: ",arr3[arr3<14]);

arr4=np.array([[18,12,19],[15,17,11]]);
print("values less than 14: ",arr4[arr4<14]);