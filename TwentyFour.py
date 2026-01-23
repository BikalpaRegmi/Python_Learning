############### Bar Plot #################
import matplotlib.pyplot as plt;
import pandas as pd;

"""
Below given in y axis is the ratings of stranger things and Seasons in x axis.
i. Create a Bar diagram with title,xlabel and ylabel.
ii.Increase the font size of Title.
iii.Change the colors of each bars & set the edge color(border of bar) as orange.
"""
y=[9,7,8,4,3];
x=["S1","S2","S3","S4","S5"];

plt.bar(x,y,color=["Red","Green","Blue","Black","Yellow"],edgecolor="orange");
plt.xlabel("Seasons of Strangers Things");
plt.ylabel("My Ratings as Star out of 10");
plt.title("Stranger things ratings per seasons",fontsize=20);
plt.show();



"""
Wap to import an excel file and visualize its datas as Bar diagram.
"""
data=pd.read_excel("C:/Users/user/OneDrive - Hetauda School of Management and Social Sciences/Desktop/Data Analysis/Pandas Practice Excel/demo_pandas_practice_xslx.xlsx");
df=pd.DataFrame(data);

groupedBy = df.groupby("Department")["Score"].sum();
print(groupedBy);

x=groupedBy.index;
y=groupedBy.values;

plt.bar(x,y,edgecolor="gray");
plt.title("Scores of different departments",fontsize=20);
plt.xlabel("Departments");
plt.ylabel("Scores");
plt.show();