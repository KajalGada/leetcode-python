class Solution:
    
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        # swap so nums1 is small
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1
            
        len1 = len(nums1)
        len2 = len(nums2)
        
        # Mid point of combined array
        len_comb = len1 + len2
        len_comb_half = len_comb//2
        
        odd = (len_comb)%2
        ans = 0.0
            
        # Left and right for nums 1
        left_ind = 0
        right_ind = len1 - 1

        while True:

            # Get partitions
            part1_ind = (left_ind + right_ind)//2
            
            # part1_size = part1_ind + 1
            # part2_ind = (len_comb_half - part1_size) - 1  
            # (-1) cause index starts at 0
            part2_ind = len_comb_half - part1_ind - 2

            # Get numbers left and right of partition
            part1_left = float('-infinity')
            if part1_ind >= 0:
                part1_left = nums1[part1_ind]

            part1_right = float('infinity')
            if (part1_ind + 1) < len1:
                part1_right = nums1[part1_ind + 1]

            part2_left = float('-infinity')
            if part2_ind >= 0:
                part2_left = nums2[part2_ind]

            part2_right = float('infinity')
            if (part2_ind + 1) < len2:
                part2_right = nums2[part2_ind + 1]

            if (part1_left <= part2_right) and (part2_left <= part1_right):

                if odd:
                    ans = min(part1_right, part2_right)
                else:
                    ans = (max(part1_left, part2_left) + min(part1_right, part2_right))/2
                break

            elif part1_left > part2_right:
                right_ind = part1_ind - 1

            else:
                left_ind = part1_ind + 1
        
        return ans
