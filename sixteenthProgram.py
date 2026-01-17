################################## Importing csv and excel in Pandas #####################################

import pandas as pd;

# Wap to convert Dictonary to DataFrame.
dct = {"Name":["Bikalpa","Binayak","Bidhaika","Bibek"],
       "Age": [20,19,18,20]};
df = pd.DataFrame(dct);
print(df);

print("\n\n\n")

# Wap to add csv file in python.
data=pd.read_csv("C:/Users/user/OneDrive - Hetauda School of Management and Social Sciences/Desktop/Data Analysis/Pandas Practice Excel/demo_pandas_practice_CSV.csv");
print(data);

print("\n\n\n")

# Wap to import excel(xlsx) file in pandas.
data=pd.read_excel("C:/Users/user/OneDrive - Hetauda School of Management and Social Sciences/Desktop/Data Analysis/Pandas Practice Excel/demo_pandas_practice_xslx.xlsx");
print(data);


