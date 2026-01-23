############# Line Plot ################

import pandas as pd;
import matplotlib.pyplot as plt;

# Wap to show the line plotting along with use of different parameters.
days = ["Sun","Mon","Tue","Wed","Thu","Fri","Sat"];
peoples_week1 = [40,55,63,39,80,55,48];
peoples_week2 = [33,16,65,35,32,20,27];

plt.plot(days,peoples_week1,marker="o",color="orange",label = "Week1",alpha=0.3);
plt.plot(days,peoples_week2,marker="*",color="red",ls="--",label = "Week2");
plt.legend();
plt.xlabel("Days of weeks");
plt.ylabel("No of peoples attended cafe");
plt.title("Weekly report of Peoples coming to cafe");
plt.show();



# Wap to import a ESD excel file and check which country provides greater salaries then perform line plotting.
data=pd.read_excel("C:/Users/user/OneDrive - Hetauda School of Management and Social Sciences/Desktop/Data Analysis/Pandas Practice Excel/ESD.xlsx");
df = pd.DataFrame(data);

groupedBy = df.groupby("Country")["Annual Salary"].sum();

plt.plot(groupedBy.index,groupedBy.values,marker="o");

plt.show();