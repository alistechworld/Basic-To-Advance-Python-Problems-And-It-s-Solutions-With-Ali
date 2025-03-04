class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        # Base Case: If list1 is empty, return other list
        if not list1:
            return list2
        if not list2:
            return list1
        
        # Recursion Case: Attach the smaller node and call function for next nodes
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2

# Helper function to convert a Python list to a linked list
def list_to_linkedlist(lst):
    dummy = ListNode()
    current = dummy
    for value in lst:
        current.next = ListNode(value)
        current = current.next
    return dummy.next

# Helper function to convert a linked list to a Python list
def linkedlist_to_list(node):
    lst = []
    while node:
        lst.append(node.val)
        node = node.next
    return lst

# Create an instance of the Solution class
obj = Solution()

# Convert Python lists to linked lists
list1 = list_to_linkedlist([1, 2, 4])
list2 = list_to_linkedlist([1, 3, 4])

# Merge the two linked lists
merged_list = obj.mergeTwoLists(list1, list2)

# Convert the merged linked list back to a Python list
result = linkedlist_to_list(merged_list)

print(result)  # Output: [1, 1, 2, 3, 4, 4]