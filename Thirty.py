################## Sub plotting & Saving the Diagram ###################
import matplotlib.pyplot as plt
import pandas as pd;

"""
WAP to demonstrate any 4 figure in subplots. Use ESD excel file.
1. Gender and number peoples(EEID) Bar diagram.
2. Asian Ethnicity in each City Pie chart.
3. Annual Salary Distribution by Department & Country
4. Violin plotting of different ages of employees by Countries.
"""

data=pd.read_excel("C:/Users/user/OneDrive - Hetauda School of Management and Social Sciences/Desktop/Data Analysis/Pandas Practice Excel/ESD.xlsx");
print(data.columns);

fig, ax = plt.subplots(2, 2, figsize=(12, 9));

gender_count = data.groupby("Gender")["EEID"].count()
ax[0,0].bar(gender_count.index, gender_count.values)
ax[0,0].set_title("Gender vs Number of Employees")
ax[0,0].set_xlabel("Gender")
ax[0,0].set_ylabel("Count")


asian_city = data[data["Ethnicity"]=="Asian"].groupby("City")["EEID"].count()
ax[0,1].pie(asian_city.values, labels=asian_city.index, autopct="%1.1f%%")
ax[0,1].set_title("Asian Employees by City")


countries = data["Country"].unique()
departments = data["Department"].unique()
y_series = []
for dept in departments:
    dept_salaries = []
    for country in countries:
        total = data[(data["Department"]==dept) & (data["Country"]==country)]["Annual Salary"].sum()
        dept_salaries.append(total)
    y_series.append(dept_salaries)
ax[1,0].stackplot(range(len(countries)), y_series, labels=departments)
ax[1,0].set_xticks(range(len(countries)))
ax[1,0].set_xticklabels(countries)
ax[1,0].set_title("Annual Salary Distribution by Department & Country")
ax[1,0].set_xlabel("Country")
ax[1,0].set_ylabel("Total Annual Salary")
ax[1,0].legend(loc="upper right")


age_groups = [group["Age"].values for name, group in data.groupby("Country")]
country_labels = data["Country"].unique()
ax[1,1].violinplot(age_groups)
ax[1,1].set_xticks(range(1, len(country_labels)+1))
ax[1,1].set_xticklabels(country_labels)
ax[1,1].set_title("Age Distribution by Country")
ax[1,1].set_ylabel("Age")


plt.savefig("C:/Users/user/OneDrive - Hetauda School of Management and Social Sciences/Pictures/Screenshots/FinalFig.png");
plt.tight_layout()
plt.show()