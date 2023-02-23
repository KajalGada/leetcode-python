class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        nums_set_sum = sum(set(nums))
        nums_sum = sum(nums)

        len_nums = len(nums)

        dup_num = nums_sum - nums_set_sum
        exp_sum = ((len_nums)*(len_nums+1))/2
        missing_num = int(exp_sum - nums_set_sum)


        return [dup_num, missing_num]
