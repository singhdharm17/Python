"""13. Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check
whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated
sequence. """

n_list = []
s_num = input("Enter the number separated by commas:- ")
s_num = s_num.split(",")
# print(s_num)
for i in s_num:
    # print(i)
    i_temp = int(i, 2)
    if i_temp % 5 == 0:
        n_list.append(f"{i}")
print(",".join(n_list))
