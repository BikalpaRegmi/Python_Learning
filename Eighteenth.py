####################################### Handeling NaN #############################################

import numpy as np ;
import pandas as pd ;

pd.set_option("future.no_silent_downcasting", True)

# Wap to handle check the number of null values and drop the row containing NaN anywhere.
data=pd.read_csv("C:/Users/user/OneDrive - Hetauda School of Management and Social Sciences/Desktop/Data Analysis/Pandas Practice Excel/demo_pandas_practice_CSV.csv");
print(data.isnull());
print(data.isnull().sum());
print(data.dropna());

print("\n\n\n")

# Wap to replace all the NaN values with "Hello". 
data=pd.read_csv("C:/Users/user/OneDrive - Hetauda School of Management and Social Sciences/Desktop/Data Analysis/Pandas Practice Excel/demo_pandas_practice_CSV.csv");
print(data.replace(np.nan , "Hello"));

print("\n\n\n");

# Wap to replace all the NaN values existing in Score with 81.9.
data=pd.read_csv("C:/Users/user/OneDrive - Hetauda School of Management and Social Sciences/Desktop/Data Analysis/Pandas Practice Excel/demo_pandas_practice_CSV.csv");
data["Score"] = data["Score"].replace(np.nan , 81.9);
print(data);

print("\n\n\n");

# Wap to replace all NaN values existing in Score after finding its Mean.
data=pd.read_csv("C:/Users/user/OneDrive - Hetauda School of Management and Social Sciences/Desktop/Data Analysis/Pandas Practice Excel/demo_pandas_practice_CSV.csv");
print(data["Score"].mean());
data["Score"] = data["Score"].replace(np.nan , 81.2);
print(data);

print("\n\n\n");

# Wap to replace the NaN values with backward(next) filling and forward(previous) filling.
data=pd.read_csv("C:/Users/user/OneDrive - Hetauda School of Management and Social Sciences/Desktop/Data Analysis/Pandas Practice Excel/demo_pandas_practice_CSV.csv");
print("Backward Fill:")
print(data.bfill().infer_objects(copy=False))

print("\nForward Fill:")
print(data.ffill().infer_objects(copy=False))
