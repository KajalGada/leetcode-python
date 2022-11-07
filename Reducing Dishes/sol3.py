class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:        
        
        max_sat = 0
        satisfaction.sort(reverse=True)

        cur_sat = 0
        cum_sum = 0

        for each_dish in satisfaction:

            cum_sum += each_dish
            cur_sat += cum_sum
            max_sat = max(max_sat, cur_sat)

        return max_sat
