class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        if len(arr) == 1:
            return True

        arr_map = {}

        for n in arr:
            if n in arr_map:
                arr_map[n] += 1
            else:
                arr_map[n] = 1

        occ_map = {}
        ans = True

        for n in arr_map.keys():
            n_occ = arr_map[n]
            if n_occ in occ_map:
                ans = False
                break
            else:
                occ_map[n_occ] = None

        return ans
