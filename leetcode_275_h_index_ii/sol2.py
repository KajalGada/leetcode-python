class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        len_cit = len(citations)        
        st = 0
        en = len_cit - 1
        h = 0
        
        while st <= en:
            
            mid = st + ((en-st)//2)
            h_cand = citations[mid]
            num_paper = len_cit - mid
            
            if h_cand == num_paper:
                h = h_cand
                break
                
            elif h_cand < num_paper:
                st += 1
                
            else:
                h = max(h, num_paper)
                en -= 1
                
        return h
        
