class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        res = True
        if len(s) != len(t):
            res = False
            
        else:
            
            if sorted(s) != sorted(t):
                res = False
        
        return res
        
