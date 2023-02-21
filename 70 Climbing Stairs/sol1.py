class Solution:
    def climbStairs(self, n: int) -> int:

        if n < 3:
            return n

        n1 = 1
        n2 = 2

        for _ in range(3, n+1):
            n3 = n1 + n2
            n1 = n2
            n2 = n3

        return n3
