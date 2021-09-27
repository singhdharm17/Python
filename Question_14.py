"""14. Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9"""

str1 = input("Enter the String:- ")
result = {"Upper": 0, "Lower": 0}
for i in str1:
    if i.isupper():
        result["Upper"] += 1
    elif i.islower():
        result["Lower"] += 1
print("Upper Case", result["Upper"])
print("Lower Case", result["Lower"])

