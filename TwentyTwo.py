######################## Copy & Comparison #############################

import pandas as pd;

dict = {"Phones":["Apple","Realme","Redmi","Samsung"],
        "Price":[1000,400,300,900],
        "Quantity":[10,30,35,16]};

df = pd.DataFrame(dict);
print(df);

print("\n\n\n");

df1=df.copy();"""Copying"""

print(df1);

print("\n");

df1.loc[0,"Price"]=1100;
df1.loc[2,"Price"]=280;
df1.loc[2,"Quantity"]=48;

print(df.compare(df1));"""Default Comparison"""

print("\n\n\n");

print(df.compare(df1 , align_axis=0));"""Compares Vertically"""

print("\n\n\n");

print(df.compare(df1 , keep_equal=True)); """Removes unnecessary NaN from other column whom are equal"""

print("\n\n\n");

print(df.compare(df1 , keep_shape=True)); """Shows every column but NaN which are not changed"""