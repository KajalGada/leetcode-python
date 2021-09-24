class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        
        nums.sort()
        len_nums = len(nums)
        ans = (nums[len_nums-1]*nums[len_nums-2]) - (nums[0]*nums[1])
        
        return ans
