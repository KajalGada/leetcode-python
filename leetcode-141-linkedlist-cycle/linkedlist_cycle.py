# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        
        has_cycle_flag = False
        fast = head
        
        while fast and fast.next:
            
            head = head.next
            fast = fast.next.next

            if head is fast:
                has_cycle_flag = True
                break
            
        return has_cycle_flag
