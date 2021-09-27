# Data of XYZ company is stored in sorted list. Write a program for searching specific data from that list.

c_data = input("Enter the data separated by commas:-")
print("Company List has been created")
list_c_data = str(c_data).split(",")  # converting list into list by delimiter
f_data = input("Enter the item need to searched in Company data:- ")

if f_data in list_c_data:
    print(f"{f_data} is present in given list at {list_c_data.index(f_data)+1}")
else:
    print(f"{f_data} is not present is given list")
