class Solution:
    def reverseBits(self, num: int) -> int:

        num = ((num & 0xFFFF0000) >> 16) | ((num & 0x0000FFFF) << 16)
        num = ((num & 0xFF00FF00) >> 8) | ((num & 0x00FF00FF) << 8)
        num = ((num & 0xF0F0F0F0) >> 4) | ((num & 0x0F0F0F0F) << 4)

        num = ((num & 0xcccccccc) >> 2) | ((num & 0x33333333) << 2)
        num = ((num & 0xaaaaaaaa) >> 1) | ((num & 0x55555555) << 1)

        return num
