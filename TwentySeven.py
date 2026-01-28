################ PieChart Plotting ##################
import pandas as pd;
import matplotlib.pyplot as plt;

"""
Wap to make a pyChart. Use different parameters.
"""
sub=["BIM","BCA","BBS","BBA","BSC CSIT"];
no_of_std=[60,40,35,55,23];
color = ["Red","Green","Blue","Black","Purple"];
exp = [0.1,0,0,0,0];
plt.pie(no_of_std,labels=sub,colors=color,explode=exp,autopct="%.2f",shadow=True);
plt.savefig("Piechart.png");
plt.show();



"""
Wap to make pyChart of a ESD excel file. Make piechart on basis of department label and salary.
"""
data=pd.read_excel("C:/Users/user/OneDrive - Hetauda School of Management and Social Sciences/Desktop/Data Analysis/Pandas Practice Excel/ESD.xlsx");
df = pd.DataFrame(data);
print(df.columns);
department_Salary = df.groupby("Department")["Annual Salary"].sum();
print(department_Salary);
plt.pie(department_Salary.values,labels=department_Salary.index,autopct="%.2f");
plt.show();



"""
Wap to make pyChart of a ESD excel file. Make piechart on basis of department label and number of employees.
"""
data=pd.read_excel("C:/Users/user/OneDrive - Hetauda School of Management and Social Sciences/Desktop/Data Analysis/Pandas Practice Excel/ESD.xlsx");
df = pd.DataFrame(data);
department_Jobs = df.groupby("Department")["EEID"].count();
print(department_Jobs);
plt.pie(department_Jobs.values,labels=department_Jobs.index,autopct="%.2f");
plt.show();
