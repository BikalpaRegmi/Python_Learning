############################### Exploring big datas in Pandas ######################################

import pandas as pd;

# """ Below given file is a 1000 line of excel data.
#     # WAP to print datas from 0-4 and 995-1000.
#     # Wap to Describe the conclusion of the excel data.
#     # Wap to print its Statical data of each numeric values.
#     # Wap to check the sum of null values each column.
# """
# data=pd.read_excel("C:/Users/user/OneDrive - Hetauda School of Management and Social Sciences/Desktop/Data Analysis/Pandas Practice Excel/ESD.xlsx");
# print("Top 5 values-:");
# print(data.head(5));
# print("\n\n\n","Bottom 5 values-:");
# print(data.tail(5));
# print("\n\n\n","Conclusion of excel file-:");
# print(data.info());
# print("\n\n\n","Stats of each numeric column-:");
# print(data.describe());
# print("\n\n\n","Total number of null on each column-:");
# print(data.isnull().sum());



# Wap to handle duplicate of primary keys in pandas.
data=pd.read_csv("C:/Users/user/OneDrive - Hetauda School of Management and Social Sciences/Desktop/Data Analysis/Pandas Practice Excel/demo_pandas_practice_CSV.csv");
print(data);
print("\n\n", "Handling duplicate row-:");
print(data.duplicated());
print("\n\n", "Handling duplicate values in a column-:");
print(data.duplicated("ID"));
print("\n\n", "Sum of duplicated values in a column-:");
print(data.duplicated("ID").sum());
print("\n\n", "After Removing duplicated values in ID column-:");
print(data.drop_duplicates("ID"));