# write a python program to find the second largest element in a give list

numbers = [10, 20, 4, 45, 99, 99, 78]

unique_numbers = list(set(numbers))

unique_numbers.sort(reverse=True)

if len(unique_numbers) > 1:
    print("The second largest number is:", unique_numbers[1])
else:
    print("No second largest number found.")    