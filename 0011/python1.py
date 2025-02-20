# Python Program to Check if Two Strings are Anagrams

def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)


word1 = str(input("Enter your first word:"))
word2 = str(input("Enter your second word:"))

if are_anagrams(word1, word2):
    print("The string is anagrams")
else:  
    print("The string is not anagrams")  
