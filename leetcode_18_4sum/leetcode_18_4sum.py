class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort()
        dict_2d = {}
        quad = []
        
        for i1, n1 in enumerate(nums):
            for i2, n2 in enumerate(nums[i1+1:]):
                
                tmp_sum = n1 + n2
                pair = [i1,  i1+i2+1]
                
                if tmp_sum in dict_2d:
                    dict_2d[tmp_sum].append(pair)
                else:
                    dict_2d[tmp_sum] = [pair]
                    
        # print(dict_2d)
        for each_sum in dict_2d:

            rem_num = target - each_sum
            
            if rem_num in dict_2d:
                
                sum_pairs = dict_2d[each_sum]
                rem_pairs = dict_2d[rem_num]
                
                for p1 in sum_pairs:
                    for p2 in rem_pairs:
                        
                        if len(set(p1+p2)) == 4:
                            
                            res_quad = [nums[p1[0]], nums[p1[1]], nums[p2[0]], nums[p2[1]]]
                            res_quad.sort()
                            if res_quad not in quad:
                                quad.append(res_quad)
                        
        return quad
        
