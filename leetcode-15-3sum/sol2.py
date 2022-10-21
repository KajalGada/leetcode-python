class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        nums_len = len(nums)
        
        # No point in looking at all positive numbers for sum = 0
        # Only look until (n-2) so you can have a triplet
        limit_i = 0
        while (nums[limit_i] <= 0) and (limit_i < (nums_len-2)):
            limit_i += 1
            
        # variables
        ans = []
        i = 0
        j = 1
        k = 2
        
        while i < limit_i:
            
            n1 = nums[i]
            
            j = i + 1
            k = nums_len - 1
            
            # 2 sum problem
            while j < k:
                
                n2 = nums[j]
                n3 = nums[k]
                
                nums_sum = n1 + n2 + n3
                
                if nums_sum == 0:
                    
                    ans.append([n1, n2, n3])
                    
                    while (j < nums_len) and (nums[j] == n2):
                        j += 1
                        
                    while (k > 0) and (nums[k] == n3):
                        k -= 1
                        
                elif nums_sum < 0:
                    
                    while (j < nums_len) and (nums[j] == n2):
                        j += 1
                        
                else:
                    
                    while (k > 0) and (nums[k] == n3):
                        k -= 1
            
            # Skip same numbers to avoid duplicates
            while (i < limit_i) and (nums[i] == n1):
                i += 1
        
        return ans
        
