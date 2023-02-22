class Solution:
    def canJump(self, nums: List[int]) -> bool:

        ans = True
        len_nums = len(nums)
        far_pos = 0

        for cur_pos, jumps in enumerate(nums):
            if far_pos < cur_pos:
                ans = False
                break

            far_pos = max(far_pos, (cur_pos + jumps))

        return ans
