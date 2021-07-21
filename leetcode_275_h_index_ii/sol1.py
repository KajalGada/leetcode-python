class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        n = len(citations)
        st = 0
        en = n - 1
        h = -1
        
        while st <= en:
            
            mid = st + ((en-st)//2)
            num_paper = n - mid
            num_cit = citations[mid]
            
            if num_paper == num_cit:
                h = num_cit
                break
                
            elif num_paper > num_cit:
                st = mid + 1
                
            else:
                en = mid - 1
                
        if h == -1:
            h = n - st
                
        return h
        
