# Write a program to print  5th  fibinocci number using Recursion
def fib(n):
    if (n==1 or n==2):
        return n-1
    return fib(n-1)+fib(n-2)
print(fib(7))