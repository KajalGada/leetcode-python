class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        
        # Dishes can be prepared in any order, 
        # so max return by preparing most satisfying dish last
        satisfaction.sort()
        
        # Trick, sum of all satifaction should be zero or more
        cur_sum = sum(satisfaction)
        
        while cur_sum < 0:
            last_num = satisfaction.pop(0)
            cur_sum -= last_num
            
        # Compute satisfaction level
        satisfaction_level = 0
        for ind, val in enumerate(satisfaction):
            satisfaction_level += (val * (ind+1))
            
        return satisfaction_level
