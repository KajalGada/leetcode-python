# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        
        nodes_eval = []
        if root.left or root.right:
            nodes_eval.append(root)
            nodes_target = []
            
            # Get all nodes with val of target
            while nodes_eval:
                
                par_node = nodes_eval.pop(0)
                
                if par_node.left:
                    nodes_eval.append(par_node.left)
                    if par_node.left.val == target:
                        nodes_target.append([par_node, par_node.left, 'left'])
                    
                if par_node.right:
                    nodes_eval.append(par_node.right)
                    if par_node.right.val == target:
                        nodes_target.append([par_node, par_node.right, 'right'])
                    
                    
            # Remove leaves
            while nodes_target:
                
                par_node, child_node, dir_node = nodes_target.pop()
                    
                if (child_node.left == None) and (child_node.right == None):
                    if dir_node == 'left':
                        par_node.left = None
                    else:
                        par_node.right = None
                        
        if root.val == target:
            if root.left == None and root.right == None:
                root = None
                
        return root
                        
                
