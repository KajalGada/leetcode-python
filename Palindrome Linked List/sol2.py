# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        rev = None
        slow = head
        fast = head
        
        # Slow moves one step, fast moves 2 step.
        # When fast reachs end, slow is at midpoint
        # Reverse => reverse the node links 1->2->3 => 1<-2<-3
        while fast and fast.next:
            
            fast = fast.next.next
            
            tmp = slow
            slow = slow.next
            tmp.next = rev
            rev = tmp
            
        # odd cases: 1-2-3-2-1 slow is at 3, send it to 2.
        if fast:
            slow = slow.next
            
        ans = True
        
        # Compare 1st half and 2nd half
        while slow and rev:
            
            if slow.val != rev.val:
                ans = False
                break
                
            slow = slow.next
            rev = rev.next
            
        return ans
            
        
