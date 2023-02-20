class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:

        ans = True
        count_5 = 0
        count_10 = 0

        for bill in bills:

            if bill == 5:
                count_5 += 1

            elif bill == 10:
                if count_5:
                    count_5 -= 1
                    count_10 += 1
                else:
                    ans = False
                    break

            else:
                if count_10 and count_5:
                    count_10 -= 1
                    count_5 -= 1

                elif (count_5 > 2):
                    count_5 -= 3

                else:
                    ans = False
                    break

        return ans
