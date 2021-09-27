"""12. Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
hello
Then, the output should be:
again and hello makes perfect practice world"""

lines = []  # List
while True:
    str1 = input('Enter lines:')
    if str1:  # string
        str1 = str1.split(" ")  # converted into list
        lines = lines + str1  # concat
    # for i in lines:
    # print("i", i)
    # if i  not in  final_list:
    #  final_list.append(i)
    else:
        break
# print("Lines", lines)
s_set = set(lines)
l_list = list(s_set)
l_list.sort()
print(" ".join(l_list))
"""str1 = (input("Enter the string :- ")).split(" ")
str2 = set(str1)
l_List=list(str2)
l_List.sort()
print(" ".join(l_List))"""
