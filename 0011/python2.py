# Write a Python program to find the factorial of a number using recursion.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
 
num = int(input("Enter the Number:"))

factorial(num)

print(f"The Factorial of {num} is ", factorial(num))  