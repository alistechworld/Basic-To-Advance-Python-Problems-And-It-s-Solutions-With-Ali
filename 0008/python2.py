num = 29
is_prime = True

if num > 1:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:  
            is_prime = False
            break
else:
    is_prime = False

if is_prime:
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")
