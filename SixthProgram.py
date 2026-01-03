
################################# DICTIONARY & Json #############################################


# Convert the following dictionary into json format. 
# Access the value of age from given data. 
# Pretty Print the following json data.
# Sort the following Json keys and add them into a file.
# Access the nested key marks of math from the data.

# Student_data = {"name":"Alice", "age" : 13, "marks" : {"math" : 99,}}

import json ;
Student_data = {"name":"Alice", "age" : 13, "marks" : {"math" : 99,}} ;
print(type(Student_data));

data = json.dumps(Student_data);
print (type(data));
print(data);

jsonData = json.loads(data);
print(jsonData["age"])

prettyData = json.dumps(Student_data, indent=4,separators=("," , '='));
print(prettyData);

f = open("Demo.json" , "w");
writeDate = json.dumps(Student_data , indent=4, sort_keys=True);
f.write(writeDate);
print("The Student Data has been written sucessfully.");

dataAccess=json.loads(data);
print("Marks of Alice: ",dataAccess["marks"]["math"]); 


# WAP to sort the dictionary by value. multiply all those values.
a={"a":12 , "c":9 , "b" : 20 , "d": 16 ,"e" : 3}
a=sorted(a.values());
print("Sorted values: ",a);


w=1;
for i in range(0,5):
    w*=a[i];
print("Multiplied value: ", w);


# WAP to print a dictionaries where the keys are the numbers between 1 & 15 and the values are square of the keys.
a={};
for i in range (1,16):
    a[i]=i*i ;
print(a);