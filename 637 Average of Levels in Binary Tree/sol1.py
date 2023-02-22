# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        ans = []
        queue = [root]

        while queue:

            tot = 0
            count = len(queue)
            new_queue = []

            for node in queue:

                tot += node.val

                if node.left:
                    new_queue.append(node.left)

                if node.right:
                    new_queue.append(node.right)

            ans.append(tot/count)
            queue = new_queue

        return ans

                
