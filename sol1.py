# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        # BTS in order is [left_node, current_node, right_node]
        # Keep going left until end aka left_most node to find lowest element
        # To find 2nd lowest element you look at current node which is last on stack.
        # To find 3rd lowest element you look at the right node.

        tmp_node = TreeNode(val=0, left=None, right=root)
        stack = []

        root = tmp_node

        for _ in range(k):
            root = root.right
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()

        return root.val
                
