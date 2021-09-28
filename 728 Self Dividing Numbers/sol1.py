class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        
        ans = []
        
        for n in range(left, right+1):
            
            self_div = True
            cur_num = n
            
            while self_div and (cur_num > 0):
                
                digit = cur_num % 10
                cur_num = cur_num//10
                
                if (digit == 0) or (n % digit) != 0:
                    self_div = False
                    
            if self_div:
                ans.append(n)
            
            
        return ans
        
