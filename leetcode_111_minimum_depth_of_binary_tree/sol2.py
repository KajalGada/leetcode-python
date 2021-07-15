# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        
        if not root:
            return 0
        
        min_depth = 0             
        nodes_explore = [[root, 1]]

        while nodes_explore:

            cur_node, cur_depth = nodes_explore.pop(0)

            if (cur_node.left is None) and (cur_node.right is None):
                min_depth = cur_depth
                break

            if cur_node.left:
                nodes_explore.append([cur_node.left, cur_depth+1])

            if cur_node.right:
                nodes_explore.append([cur_node.right, cur_depth+1])
                    
                    
        return min_depth
        
