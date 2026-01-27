############## Stem,Stack & Step plotting ##################

import pandas as pd;
import matplotlib.pyplot as plt;

"""
Wap to demonstrate the Steam.
"""
dta=[10,12,14,15,14,17,20,13,14,11,16,11,18,16,19,12,15,16,18,11,12,19,10];
plt.stem(dta);
plt.title("Demo Vertical orientiation");
plt.show();
plt.stem(dta , orientation='horizontal' , linefmt="--");
plt.title("Demo Horizontal orientiation");
plt.show();



"""
Wap to demonstrate Stem in large excel file.
"""
data=pd.read_excel("C:/Users/user/OneDrive - Hetauda School of Management and Social Sciences/Desktop/Data Analysis/Pandas Practice Excel/ESD.xlsx");
plt.stem(data["Age"] , orientation="horizontal", markerfmt="*");
plt.xlabel("Ages of employees");
plt.ylabel("All employees plotted.");
plt.title("The Stem Plotting of all employees");
plt.show();


"""
WAP to demonstrate Stack plotting in the weeks and no of peoples.
"""
weekDays = ["Sun","Mon","Tue","Wed","Thu","Fri","Sat"];

nop1=[10,80,60,70,50,40,9];
nop2=[16,83,45,50,80,42,8];
nop3=[13,68,62,78,55,60,5];
nop4=[6,81,55,67,5,48,3];
label = ["Week1" , "Week2", "Week3", "Week4"] ;

plt.stackplot(weekDays,nop1,nop2,nop3,nop4,labels=label);
plt.legend();
plt.show();


"""
WAP to demonstrate Step plotting in the excel file.
"""
data = pd.read_excel("C:/Users/user/OneDrive - Hetauda School of Management and Social Sciences/Desktop/Data Analysis/Pandas Practice Excel/demo_pandas_practice_xslx.xlsx");
grouped = data.groupby("Department")["Score"].sum();
plt.step(grouped.index,grouped.values,marker="o");
plt.show();