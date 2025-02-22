# Write a python program to generate a list of the first n Fibonacci numbers.

def fibonacci(n):
    fib_list = [0, 1]
    for i in range(2, n):
        fib_list.append(fib_list[-1] + fib_list[-2])
    return fib_list
    
n = 10
print("Fibonacci Series:", fibonacci(n))    