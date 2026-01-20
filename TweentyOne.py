####################### Merge & Concatenate ##########################

import pandas as pd;


# WAP to merge any two data frames.
data1 = {"EID" : ["01","02","03","04"],
         "Names":["Gagan","Saujan","Ritesh","Bidhan"]};
data2 = {"EID":["01","02","03","04"],
         "Salary":["100","200","300","400"]};

df1 = pd.DataFrame(data1);
df2 = pd.DataFrame(data2);

print(pd.merge(left = df1,right = df2, on="EID"))

print("\n\n\n");

# WAP to merge any two rough data frames.
data1 = {"EID" : ["01","02","03","04"],
         "Names":["Gagan","Saujan","Ritesh",""]};
data2 = {"EID":["01","02","03","04"],
         "Salary":["100","","300","400"]};

df1 = pd.DataFrame(data1);
df2 = pd.DataFrame(data2);

print(pd.merge(left = df1,right = df2, on="EID" , how="left"));

print("\n\n\n");

# WAP to concatenate a new values inside a dataframe.
data1 = {"EID" : ["01","02","03","04"],
         "Names":["Gagan","Saujan","Ritesh","Bidhan"]};
data2 = {"EID":["01","02","03","04"],
         "Salary":["100","200","300","400"]};

df1 = pd.DataFrame(data1);
df2 = pd.DataFrame(data2);
df3 = pd.merge(left = df1,right = df2, on="EID");

data3 = {"EID" : ["05","06","07","08"],
         "Names":["Alice","Bob","Charlie","David"],
         "Salary":["100","200","300","400"]};

df4 = pd.DataFrame(data3);

print(pd.concat([df3,df4]));
