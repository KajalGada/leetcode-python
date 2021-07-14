# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        val1 = 0
        while l1:
            val1 *= 10
            val1 += l1.val
            l1 = l1.next
            
        val2 = 0
        while l2:
            val2 *= 10
            val2 += l2.val
            l2 = l2.next
        
        sum_num = val1 + val2
        head = None
        if sum_num == 0:
            head = ListNode(val=0)
        
        else:
            while sum_num > 0:
                tmp_node = ListNode(val=sum_num%10)
                tmp_node.next = head
                head = tmp_node

                sum_num = sum_num//10

        return head
