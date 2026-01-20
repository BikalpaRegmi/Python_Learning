######################### Grouping in pandas #################################

import pandas as pd ;

data = pd.read_excel("C:/Users/user/OneDrive - Hetauda School of Management and Social Sciences/Desktop/Data Analysis/Pandas Practice Excel/ESD.xlsx");
print(data);

print("\n\n\n")

# Wap to print the count of Genders CountryWise.
gp = data.groupby(["Country" , "Gender"]).agg({"EEID" : "count"});
print(gp);

print("\n\n\n");

# WAP to print the Mean,Max and Min of annualSalary Ethnicity wise.
gp1 = data.groupby("Ethnicity")["Annual Salary"].agg(["mean" , "min" , "max"]);
print(gp1);