class Solution:
    def reverse(self, x: int) -> int:
        
        sign = 1
        if x < 0:
            sign = -1
            x = x * sign
            
        ans = 0
        while x > 0:
            digit = x % 10
            ans *= 10
            ans += digit
            x = x//10
            
        ans = ans * sign
        
        max_num = 2**31
        if (-1*max_num) <= ans <= (max_num - 1):
            return ans
        return 0
