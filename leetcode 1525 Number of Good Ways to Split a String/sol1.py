class Solution:
    
    def computeUnique(self, s: str) -> list[int]:
        
        letters_map = {}
        uniq_letters = []
        count = 0
        
        for ch in s:
            if ch not in letters_map:
                count += 1
                letters_map[ch] = 0
            uniq_letters.append(count)
            
        return uniq_letters
    
    def numSplits(self, s: str) -> int:

        uniq_letters = self.computeUnique(s)
        uniq_letters_reverse = self.computeUnique(s[::-1])
        uniq_letters_reverse = uniq_letters_reverse[::-1]
        
        ans = 0
        for ind in range(len(s)-1):
            good_str = uniq_letters[ind] == uniq_letters_reverse[ind+1]
            ans += good_str
        
        return ans
