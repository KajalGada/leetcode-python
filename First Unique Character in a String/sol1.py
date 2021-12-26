class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        s_map = {}
        
        for ind, ch in enumerate(s):
            
            if ch in s_map:
                s_map[ch] += 1
                
            else:
                s_map[ch] = 1
                
        ind = -1
        len_s = len(s)
        
        for s_ind in range(len_s):
            
            if s_map[s[s_ind]] == 1:
                ind = s_ind
                break
                
        return ind
                
            
