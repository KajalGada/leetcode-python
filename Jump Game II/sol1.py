class Solution:
    def jump(self, nums: List[int]) -> int:

        min_jump = 0

        rev_num = nums[::-1]

        while len(rev_num) > 1:

            max_num = 0

            for ind in range(1, len(rev_num)):

                if ind <= rev_num[ind]:
                    max_num = max(max_num, ind)

            rev_num = rev_num[max_num:]
            min_jump += 1

        return min_jump
