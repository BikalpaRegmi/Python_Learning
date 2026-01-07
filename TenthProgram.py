################################ Numpy ####################################

import numpy as np ;

# Wap to convert list to array.
list=[10,20,30,40,50];
arr = np.array(list);
print(arr);



# Wap to create multidimensional array.
lst=[[10,20],[20,30],[30,40],[40,50]];
arr1 = np.array(lst);
print(arr1)



# Wap to perform slicing on single dimensional array.
ls=[11,22,33,44,55,66,77,88,99];
arr2=np.array(ls);
print(arr2[2]); # 33
print(arr2[3:]); # [44 55 66 77 88 99]
print(arr2[3:5]); # [44 55]
print(arr2[:5]); # [11 22 33 44 55]
print(arr2[::-1]); # [99 88 77 66 55 44 33 22 11]
print(arr2[::2]); # [11 33 55 77 99]



# Wap to perform slicing on multi dimensional array.
ls=[[3,6,9],[12,15,18],[21,24,27]];
arr3=np.array(ls);
print(arr3[0,0:]); # [3 6 9]
print(arr3[1,::-1]); # [18 15 12]
print(arr3[2,0:3]); # [21 24 27]



# Wap to perform attributes of array.
ls=[[3,6,9],[12,15,18],[21,24,27]];
arr4=np.array(ls);
print(np.shape(arr4)); # (3, 3) // (rows,cols)
print(np.size(arr4)); # 9 // no of elements
print(np.ndim(arr4)); # 2 // rows and column are two dimensional
print(arr4.dtype); # int64  