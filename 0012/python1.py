# Find the Common Element Between Two Lists

list1 = [1,2,3,4,5]
list2 = [4,5,6,7,8]

common_elements = list(set(list1) & set(list2))

print("Common Elements", common_elements)