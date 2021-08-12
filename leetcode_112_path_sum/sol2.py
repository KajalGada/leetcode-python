# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        if root is None:
            return False
            
        nodes_explore = [[root, root.val]]
        ans = False
        
        while nodes_explore:
            
            cur_node, cur_sum = nodes_explore.pop()
            # print("cur_node.val: {}, cur_sum: {}".format(cur_node.val, cur_sum))
            
            if cur_node.left or cur_node.right:
                
                if cur_node.left:
                    nodes_explore.append([cur_node.left, cur_node.left.val + cur_sum])
                    
                if cur_node.right:
                    nodes_explore.append([cur_node.right, cur_node.right.val + cur_sum])
                
            elif cur_sum == targetSum:
                    ans = True
                    break
                    
        return ans
