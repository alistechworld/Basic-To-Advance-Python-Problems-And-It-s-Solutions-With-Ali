# Write a Python program to remove duplicate elements from a list while maintaining the original order.

def remove_duplicates(lst):
    unique_list=[]
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list


numbers = [1,2,2,3,4,4,5,6,6]

print("List without duplicates:", remove_duplicates(numbers))        