class Solution:
    def hIndex(self, citations: List[int]) -> int:

        h_ind = 0
        n = len(citations)

        start = 0
        end = n - 1

        while start <= end:

            mid = start + ((end - start)//2)
            h_cand = n - mid
            # print("mid: {}, h_cand: {}".format(mid, h_cand))

            if citations[mid] >= h_cand:
                h_ind = max(h_ind, h_cand)
                end = mid - 1

            else:
                start = mid + 1

        return h_ind
        
