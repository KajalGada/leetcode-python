class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        if len(a) < len(b):
            b, a = a, b
            
        len_a = len(a)
        len_diff = len_a - len(b)
        for _ in range(len_diff):
            b = '0' + b
        
        carry = 0
        ans = ""
        
        for ind in range(len_a-1, -1, -1):
            
            tot = carry + int(a[ind]) + int(b[ind])
            
            if tot == 0:
                ans += "0"
                carry = 0
                
            elif tot == 1:
                ans += "1"
                carry = 0
                
            elif tot == 2:
                ans += "0"
                carry = 1
                
            else:
                ans += "1"
                carry = 1
                
        if carry:
            ans += "1"
            
        return ans[::-1]
                
