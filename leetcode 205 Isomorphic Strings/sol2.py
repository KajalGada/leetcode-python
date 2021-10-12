class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        ans = True
        
        # Represents 128 ascii characters. -1 represents unmarked
        s_map = [-1] * 128
        t_map = [-1] * 128
        
        len_s = len(s)
        
        # Assign index number to character in s and t. 
        # If unseen (-1), else they should have same index number
        
        for ind in range(len_s):
            
            s_ascii = ord(s[ind])
            t_ascii = ord(t[ind])
            
            if s_map[s_ascii] != t_map[t_ascii]:
                ans = False
                break
                
            s_map[s_ascii] = ind
            t_map[t_ascii] = ind  
            
        return ans
        
