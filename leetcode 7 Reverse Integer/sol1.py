class Solution:
    def reverse(self, x: int) -> int:
        
        ans = 0
        
        sign = 1
        int_max = (2**31) - 1
        
        if x < 0:
            sign = -1
            int_max = (2**31)
            x *= sign
            
        int_max_10 = int_max//10
        
        while x > 0:
            
            digit = x % 10
            x = x//10
            
            # ans * 10 <= int_max
            # ans <= int_max//10
            if (ans > int_max_10):
                ans = 0
                break
                
            ans *= 10
            
            # ans + digit <= int_max
            # digit <= (int_max - ans)
            if digit > (int_max - ans):
                ans = 0
                break
                
            ans += digit
            
        ans *= sign
        
        return ans
        
