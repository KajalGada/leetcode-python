class Solution:
    def diStringMatch(self, s: str) -> List[int]:

        lo = 0
        h = len(s)
        ans = []

        for ch in s:
            
            if ch is 'I':
                ans.append(lo)
                lo += 1

            else:
                ans.append(h)
                h -= 1

        return ans + [lo]
