class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        max_len = 0
        char_map = {}
        start_ind = 0
        
        for ind, each_ch in enumerate(s):
            
            # Have I seen this char before?
            if each_ch in char_map:
                
                # Until now is one substring
                max_len = max(max_len, (ind - start_ind))
                
                # New substring will start from the char next to repeat char
                start_ind = max(start_ind, (char_map[each_ch]+1))
            
            char_map[each_ch] = ind
            
        # Check the last substring for max
        max_len = max(max_len, (len(s)-start_ind))
            
        return max_len
