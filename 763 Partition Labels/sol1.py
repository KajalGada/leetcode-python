class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        # Track the last occurance (ind) of each char
        ch_map = {}
        for ind, ch in enumerate(s):
            ch_map[ch] = ind

        ans = []
        st_ind = 0
        end_ind = 0

        # Loop till you reach the last occurance of all char in each part
        for ind, ch in enumerate(s):

            # Each part ends at last occurance of current char.
            end_ind = max(end_ind, ch_map[ch])

            # At the end of part, calculate its length and start a new part
            if ind == end_ind:
                ans.append(end_ind - st_ind + 1)
                st_ind = ind + 1

        return ans



