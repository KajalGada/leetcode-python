# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        if root1 and root2:

            stack_nodes = [[root1, root2]]

            while stack_nodes:

                n1, n2 = stack_nodes.pop(0)
                n1.val += n2.val

                # If both left nodes exist, add to list
                if n1.left and n2.left:
                    stack_nodes.append([n1.left, n2.left])

                # Else merge it into tree1
                elif n2.left:
                    n1.left = n2.left

                if n1.right and n2.right:
                    stack_nodes.append([n1.right, n2.right])

                elif n2.right:
                    n1.right = n2.right

        elif root2:
            return root2

        return root1
