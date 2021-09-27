"""10. Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world"""

s_str = input("Enter the word separated by commas:- ")
s_str = s_str.split(",")
s_str.sort()
# print(sorted(s_str))
print(",".join(s_str))