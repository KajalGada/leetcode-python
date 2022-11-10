class Solution:
    def firstUniqChar(self, s: str) -> int:

        str_map = {}

        for char in s:

            if char in str_map:
                str_map[char] += 1

            else:
                str_map[char] = 1

        ans = -1

        for ind, char in enumerate(s):

            if str_map[char] == 1:
                ans = ind
                break

        return ans
