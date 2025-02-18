# Count the Frequency of Elements in a List

from collections import Counter

number = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]

frequency_count = Counter(number)

print(f"The Frequencey count:", frequency_count)