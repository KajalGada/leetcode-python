class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        len_nums = len(nums)
        if len_nums == 1:
            return False

        nums.sort()
        ans = False

        for ind in range(1, len_nums):

            if nums[ind] == nums[ind-1]:
                ans = True
                break

        return ans
