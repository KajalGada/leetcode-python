# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:

        # from list1 to loc_a_left
        loc_a_left = list1
        for _ in range(a-1):
            loc_a_left = loc_a_left.next

        # loc_a to loc_b_right
        loc_b_right = loc_a_left.next
        for _ in range(b-a+1):
            loc_b_right = loc_b_right.next

        # add list2 to list1 at a
        loc_a_left.next = list2

        # connect list2 to list1 at b
        while list2.next:
            list2 = list2.next
        list2.next = loc_b_right
        
        return list1
