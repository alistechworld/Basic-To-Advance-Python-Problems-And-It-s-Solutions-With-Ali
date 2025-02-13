# Python Program to print the fabonacci series

n = 10 

a , b = 0 , 1
print("Printing the Fabonacci Series")
for _ in range(n):
    print(a, end=" ")
    a, b = b , a + b