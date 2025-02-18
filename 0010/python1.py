#  Count the number of vowels in a string

string = str(input("Enter the vowels:"))
vowel = "aeiouAEIOU"
count = 0

for char in string:
    if char in vowel:
        count += 1
print(f"Noumber of vowels:{count}")        