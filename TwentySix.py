####################### Scatter Plot ########################

import pandas as pd;
import matplotlib.pyplot as plt;

"""
Wap to do scatter ploting in ESD excel data. Adjust size based on Ages.
"""
data=pd.read_excel("C:/Users/user/OneDrive - Hetauda School of Management and Social Sciences/Desktop/Data Analysis/Pandas Practice Excel/ESD.xlsx");
df=pd.DataFrame(data);
print(df.columns);
x=df["Annual Salary"];
y=df["EEID"];
sizes = df["Age"];
plt.scatter(x,y,s=sizes);
plt.show();