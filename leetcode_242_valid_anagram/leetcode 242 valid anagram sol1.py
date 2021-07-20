class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        res = True
        if len(s) != len(t):
            res = False
            
        else: 
            s_map = {}
            for each_char in s:
                if each_char in s_map:
                    s_map[each_char] += 1
                else:
                    s_map[each_char] = 1
                    
            for each_char in t:
                if each_char in s_map:
                    s_map[each_char] -= 1
                    if s_map[each_char] < 0:
                        res = False
                        break
                        
                else:
                    res = False
                    break
        
        return res
