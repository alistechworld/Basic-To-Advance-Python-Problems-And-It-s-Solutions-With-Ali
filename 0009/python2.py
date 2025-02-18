# Check if the string is palindrome or not

word = str(input("Enter the string:"))

if word == word[::-1]:
    print(f"{word} is palindrome")
else:
    print(f"{word} is not palindrome")    