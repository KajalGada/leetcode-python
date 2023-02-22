# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head and head.next:

            cur_node = head
            head = head.next

            prev = ListNode()

            # Loop
            while cur_node and cur_node.next:

                next_node = cur_node.next
                cur_node.next = cur_node.next.next
                
                next_node.next = cur_node
                prev.next = next_node
                
                prev = cur_node
                cur_node = cur_node.next

        return head
