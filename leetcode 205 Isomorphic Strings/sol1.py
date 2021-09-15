class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        s_map = {}
        t_map = {}
        ans = True
        
        len_s = len(s)
        
        for ind in range(len_s):
            
            s_ch = s[ind]
            t_ch = t[ind]
            
            if s_ch in s_map:
                if s_map[s_ch] != t_ch:
                    ans = False
                    break
                    
                if t_map[t_ch] != s_ch:
                    ans = False
                    break
                    
            
            elif t_ch in t_map:
                ans = False
                break
                
                
            else:
                s_map[s_ch] = t_ch
                t_map[t_ch] = s_ch
                
                
        return ans
                    
