class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0
        cur_buy = prices[0]
        
        for cur_price in prices[1:]:
            
            max_profit = max(max_profit, (cur_price-cur_buy))
            cur_buy = min(cur_buy, cur_price)
            
        return max_profit
