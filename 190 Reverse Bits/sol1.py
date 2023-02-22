class Solution:
    def reverseBits(self, n: int) -> int:

        ans = 0

        for bit_pow in range(31, -1, -1):
            div = 2**bit_pow
            bit = n//div
            n = n%div

            if bit:
                rev_bit_pow = 31 - bit_pow
                ans += (2**rev_bit_pow)

        return ans
