# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        
        head = list1
        
        # Find (a-1)th node
        for _ in range(a-1):
            list1 = list1.next
            
        a_minus_1_node = list1
        
        # Now points to a
        list1 = list1.next
        
        # Attach list2 start
        a_minus_1_node.next = list2
        
        # Get to bth node
        for _ in range(b - a + 1):
            list1 = list1.next
            
        # Get end of list2
        while list2.next:
            list2 = list2.next
        
        # Attach end of list2 to list1
        list2.next = list1
        
        return head
        
