class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_org = nums[:]
        nums.sort()
        
        start_ind = 0
        end_ind = len(nums) - 1
        
        while end_ind > 0:
            
            nums_sum = nums[start_ind] + nums[end_ind]
            
            if nums_sum == target:
                break
            elif nums_sum < target:
                start_ind += 1
            else:
                end_ind -= 1
        
        org_start_ind = nums_org.index(nums[start_ind])
        
        search_start_ind = 0
        if nums[start_ind] == nums[end_ind]:
            search_start_ind = org_start_ind + 1
            
        org_end_ind = nums_org.index(nums[end_ind], search_start_ind)
        
        return [org_start_ind, org_end_ind]
