class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        
        satisfaction.sort()
        
        cum_sum = 0
        cur_sat = 0
        max_sat = 0
        len_sat = len(satisfaction)
        
        for ind in range(len_sat-1, -1, -1):
            
            cur_sat = satisfaction[ind] + cur_sat + cum_sum
            cum_sum += satisfaction[ind]
            
            max_sat = max(max_sat, cur_sat)
        
        
        return max_sat
        
