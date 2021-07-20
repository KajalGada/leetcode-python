# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
        res = True
        if root.left and root.right:
            tree1 = [root.left]
            tree2 = [root.right]
            
            while tree1:
                n1 = tree1.pop(0)
                n2 = tree2.pop(0)
                
                if n1.val != n2.val:
                    res = False
                    break
                    
                # Left node
                if n1.left and n2.right:
                    tree1.append(n1.left)
                    tree2.append(n2.right)

                elif n1.left or n2.right:
                    res = False
                    break

                # Right node
                if n1.right and n2.left:
                    tree1.append(n1.right)
                    tree2.append(n2.left)

                elif n1.right or n2.left:
                    res = False
                    break  

                
        elif root.left or root.right:
            res = False
            
        return res
