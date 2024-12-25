# Explanation of the Code:
"""The program first asks the user how many numbers they want to average.
It then uses a loop to take each number as input, 
adds them to a running total (total_sum), and calculates 
the average by dividing the total by the count of numbers (num).
Finally, it displays the calculated average."""

num = int(input("Enter your number that you want?"))
total_sum = 0
for n in range(num):
    number = float(input("Enter the number:"))
    total_sum += number
    avg = total_sum/num
print("Average of the number is:", avg)    
