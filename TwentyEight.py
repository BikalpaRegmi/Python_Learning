############### Box Plotting , Histogram Plotting & ViolinPlotting #################

import pandas as pd;
import matplotlib.pyplot as plt;

"""
Wap to show the multiple box plotting in a same diagram. 
"""
arr = [4,6,4,5,12,16,33];
arr2 = [23,26,14,25,16,33,20];
plt.boxplot([arr,arr2]);
plt.show();


"""
Wap to apply box plotting of age and annual salary in the ESD excel file.
"""
data=pd.read_excel("C:/Users/user/OneDrive - Hetauda School of Management and Social Sciences/Desktop/Data Analysis/Pandas Practice Excel/ESD.xlsx");
plt.boxplot(data["Annual Salary"]);
plt.show();
plt.boxplot(data["Age"]);
plt.show();
    

"""
Wap to apply histogram plotting of the score in demo practice pandas file.
"""
data = pd.read_excel("C:/Users/user/OneDrive - Hetauda School of Management and Social Sciences/Desktop/Data Analysis/Pandas Practice Excel/demo_pandas_practice_xslx.xlsx");
plt.hist(data["Score"],bins=10,color="pink",edgecolor="grey");
plt.show();


"""
WAP to perform violin plotting of salary and ethnicity in ESD excel file.
"""
data = pd.read_excel("C:/Users/user/OneDrive - Hetauda School of Management and Social Sciences/Desktop/Data Analysis/Pandas Practice Excel/ESD.xlsx")
groups = [group["Annual Salary"].values for name, group in data.groupby("Ethnicity")];
labels = data["Ethnicity"].unique();
plt.violinplot(groups);
plt.xticks(range(1, len(labels) + 1), labels);
plt.xlabel("Ethnicity");
plt.ylabel("Annual Salary");
plt.title("Violin Plot of Salary by Ethnicity");
plt.show();