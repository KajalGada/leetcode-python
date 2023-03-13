class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buy_flag = True
        buy_price = prices.pop(0)
        cur_profit = 0
        max_profit = 0

        for cur_price in prices:

            if buy_flag and (cur_price < buy_price):

                buy_price = cur_price

            elif buy_flag:

                cur_profit = cur_price - buy_price
                max_profit += cur_profit
                buy_flag = False

            elif (cur_price - buy_price) > cur_profit:

                max_profit -= cur_profit
                cur_profit = cur_price - buy_price
                max_profit += cur_profit

            else:

                buy_price = cur_price
                buy_flag = True

        return max_profit
        
