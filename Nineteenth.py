#################### Column Transformation ###########################

import pandas as pd ;
import numpy as np;

data = pd.read_excel("C:/Users/user/OneDrive - Hetauda School of Management and Social Sciences/Desktop/Data Analysis/Pandas Practice Excel/demo_pandas_practice_xslx.xlsx");
print(data);

print("\n\n\n");

# Wap to add a column named Status where if the Score is greater than 80 then A either ways B.
data.loc[data["Score"]<80 , "Status"] = "B" ;
data.loc[data["Score"]>=80 , "Status"] = "A" ;
data.loc[data["Score"]>=90 , "Status"] = "A+" ;
print(data);

print("\n\n\n");

# WAP to concatinate to column Passed and Status as FinalStatus. Drop the Passed and Status column EX: True (B).
data["FinalStatus"] = data["Passed"].astype(str) + " (" + data["Status"] + ")" ;
data.drop(columns=["Passed", "Status"], inplace=True)
print(data);

print("\n\n\n");

# Wap to add a new Column that gives the GPA depending on the score. After getting gpa, Remove the brackets in FinalStatus.
data["GPA"] = data["Score"]/25;
print(data); 
