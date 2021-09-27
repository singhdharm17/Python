# 7. Write a program which can compute the factorial of a given numbers. Use recursion to find it.
def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)

num=int(input("Enter the number to calculate factorial:-"))
print(factorial(num))