class Solution:
    def jump(self, nums: List[int]) -> int:

        far = 0
        end = 0
        jumps = 0
        n = len(nums)
        nums.pop()

        for ind, reach in enumerate(nums):

            far = max(far, ind+reach)

            if ind == end:
                jumps += 1
                end = far

        return jumps
