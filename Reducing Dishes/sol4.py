class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:        
        
        satisfaction.sort()

        cum_sum = sum(satisfaction)

        while cum_sum < 0:
            neg_num = satisfaction.pop(0)
            cum_sum -= neg_num

        satisfaction = satisfaction[::-1]

        cur_sat = 0
        max_sat = 0
        cum_sum = 0

        for each_dish in satisfaction:

            cum_sum += each_dish
            cur_sat += cum_sum
            max_sat = max(max_sat, cur_sat)

        return max_sat
