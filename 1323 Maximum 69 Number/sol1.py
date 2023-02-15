class Solution:
    def maximum69Number (self, num: int) -> int:

        stack = []
        mulitplier = 0
        loc = -1
        org_num = num

        while num:

            digit = num % 10
            num = num//10
            if digit == 6:
                loc = mulitplier
            mulitplier += 1

        if loc != -1:
            org_num += (3 * (10**loc))

        return org_num

        
