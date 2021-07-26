class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        nums1 = list(set(nums1))
        nums2 = list(set(nums2))
        
        nums1.sort()
        nums2.sort()
        
        res = []
        while nums1 and nums2:
            
            n1 = nums1[0]
            n2 = nums2[0]
            
            if n1 == n2:
                res.append(n1)
                nums1.pop(0)
                nums2.pop(0)
                
            elif n1 < n2:
                nums1.pop(0)
                
            else:
                nums2.pop(0)

        return res
        
