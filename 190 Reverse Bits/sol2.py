class Solution:
    def reverseBits(self, n: int) -> int:

        ans = 0

        for _ in range(32):

            # Bit shift to left means multiply by 2
            ans *= 2

            # Last bit is 2^0 = 1. So if last bit is set (1) we add 1
            if (n % 2):
                ans += 1

            # To look at next bit on right divide by 2
            n = n//2


        return ans
