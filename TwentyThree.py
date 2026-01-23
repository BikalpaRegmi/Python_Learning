################ Pivoting & Melting ##################

import pandas as pd;

# Wap to Show Pivoting of a dataframe.
dict = {"Name":["Bikalpa","Amit" , "Bikalpa","Amit"]
        ,"Subjects":["Math","Math","Science","Science"],
        "Scores":[72,69,80,55]};
df1 = pd.DataFrame(dict);
print(df1);

print("\n" , "Pivoted Data-: ");

print(df1.pivot(index="Name" , columns="Subjects" , values="Scores"));

print("\n\n\n");



# Wap to Show Pivot table of dataframe. The repeated value should result in maximim one.
df = pd.DataFrame({
    "Name": ["Bikalpa","Bikalpa","Bikalpa","Amit"],
    "Subjects": ["Math","Math","Science","Math"],
    "Scores": [85,88,90,78]
})
print(df);

print("\n" , "Pivoted Table Data-: ");

print(df.pivot_table(index="Name",columns="Subjects",values="Scores",aggfunc="max"));

print("\n\n\n");


# Wap to melt down a pivot table back to original form.
df = pd.DataFrame({
    "Name": ["Bikalpa","Amit"],
    "Math": [85,78],
    "Science": [90,88]
})
print(df);
melted = pd.melt(df,
                 id_vars="Name",
                 value_vars=["Math","Science"],
                 var_name="Subjects",
                 value_name="Scores");
print(melted);

#If you want more Rows Lesser columns you should Melt.
#If you want more columns Lesser Rows you should Pivot.