class Solution {
public:
    int maxProfit(vector<int>& arr) {
        
        if (arr.size() < 2)
        {
            return 0;
        }

        bool buy_flag = true;
        int buy_price = arr[0];
        bool sell_flag = false;
        int cur_profit = 0, total_profit = 0, cur_price = 0;

        for (int ind = 1; ind < arr.size(); ++ind)
        {
            cur_price = arr[ind];
            // If a share is purchased, see if it could have been purchased for cheaper or can be sold.
            if (buy_flag == true)
            {

                if (cur_price <= buy_price)
                {
                    buy_price = cur_price;
                }
                else
                {
                    cur_profit = cur_price - buy_price;
                    total_profit += cur_profit;
                    buy_flag = false;
                }

            }
            // If you don't have a share, see if you could have sold it for higher else buy again.
            else
            {
                if ((cur_price - buy_price) >= cur_profit)
                {
                    total_profit -= cur_profit;
                    cur_profit = cur_price - buy_price;
                    total_profit += cur_profit;
                }
                else
                {
                    buy_price = cur_price;
                    buy_flag = true;
                }
            }
        }

        return total_profit;
        
    }
};
