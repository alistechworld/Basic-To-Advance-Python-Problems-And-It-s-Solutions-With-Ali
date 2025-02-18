# Find the GCD(Greatest Common Divisor) of two numbers

def gcd(a, b):
    while b:
        a, b  = b, a % b
    return a
num1 =  int(input("Enter your first number:"))
num2 =  int(input("Enter your second number:"))

print(f"The Greatest Common Divisor of {num1} and {num2} is:", gcd(num1, num2))  