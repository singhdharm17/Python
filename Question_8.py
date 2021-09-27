"""8. Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H: C is 50. H is 30.
D is the variable whose values should be input to your program in a comma- separated sequence."""
import math

C = 50
H = 30


def Formula(D):
    Q = int(math.sqrt((2 * C * D) / H))
    return Q


print("Enter the number")
num = input(">>> ")
num = num.split(",")
result = []

for i in range(len(num)):
    f = Formula(int(num[i]))
    result.append(f)

print(result)
