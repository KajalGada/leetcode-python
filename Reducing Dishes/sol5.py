class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:        
        
        satisfaction.sort()

        # Max Sat is 0 i.e. no dishes
        max_sat = 0

        # Lets add the best dish
        cur_sat = satisfaction.pop()
        cum_sum = cur_sat

        # If it increase satisfaction, keep going
        while cur_sat > max_sat:
            max_sat = cur_sat

            # Let's add another dish (reverse order so it the best of remaining dishes)
            if satisfaction:                
                cum_sum += satisfaction.pop()
                cur_sat += cum_sum

        return max_sat
