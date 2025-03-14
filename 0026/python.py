# Problem Statement: Remove Duplicates from Sorted List
# Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the modified linked list.

# Example 1:
# Input: head = [1,2,3,3,4,4,5]
# Output: [1,2,5] 


class Solution():
    def deleteDuplicates(self, head):
        cur = head
        while cur:
            while cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next
            cur = cur.next
        return head
    
         