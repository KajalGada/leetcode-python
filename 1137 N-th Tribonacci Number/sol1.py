class Solution:
    def tribonacci(self, n: int) -> int:

        tri = [0, 1, 1]

        if n < 3:
            return tri[n]

        cum_sum = 2
        for _ in range(3, n+1):
            rmv = tri.pop(0)
            tri.append(cum_sum)
            cum_sum *= 2
            cum_sum -= rmv

        return tri[-1]
