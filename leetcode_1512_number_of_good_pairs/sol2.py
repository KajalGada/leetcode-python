class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        ans = 0
        nums_map = [0] * 101
        
        for n in nums:
            
            ans += nums_map[n]
            nums_map[n] += 1
            
        return ans
        
