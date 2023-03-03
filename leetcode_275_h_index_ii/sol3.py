class Solution:
    def hIndex(self, citations: List[int]) -> int:

        tot_pprs = len(citations)
        st_ind = 0
        en_ind = tot_pprs - 1
        h = 0

        while st_ind <= en_ind:

            mid_ind = st_ind + ((en_ind - st_ind)//2)
            h_cand = citations[mid_ind]
            num_pprs = tot_pprs - mid_ind

            if h_cand == num_pprs:
                h = h_cand
                break

            elif h_cand < num_pprs:
                st_ind = mid_ind + 1

            else:
                h = max(h, num_pprs)
                en_ind = mid_ind - 1

        return h
        
