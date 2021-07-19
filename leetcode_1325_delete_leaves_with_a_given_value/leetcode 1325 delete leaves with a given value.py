# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        
        nodes_explore = [root]
        all_nodes = []
        
        while nodes_explore:
            
            cur_node = nodes_explore.pop(0)
            
            if cur_node.left:
                all_nodes.append([cur_node, 'left', cur_node.left])
                nodes_explore.append(cur_node.left)
                
            if cur_node.right:
                all_nodes.append([cur_node, 'right', cur_node.right])
                nodes_explore.append(cur_node.right)
        
        while all_nodes:
            
            par_node, direction, cur_node = all_nodes.pop()
            
            if (cur_node.left is None) and (cur_node.right is None):
                if cur_node.val == target:
                    if direction == 'left':
                        par_node.left = None
                    else:
                        par_node.right = None
                        
        if (root.left is None) and (root.right is None):
            if root.val == target:
                root = None
            
        return root
                        
                        
                    
                        
