class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        
        res = True
        if len(nums) < 3:
            res = False
            
        else:
            
            # Count frequency
            freq_map = {}
            for each_num in nums:
                if each_num in freq_map:
                    freq_map[each_num] += 1
                else:
                    freq_map[each_num] = 1
                    
            # Create subsequences
            hyp_map = {}
            for n in nums:
                
                if freq_map[n] > 0:
                    freq_map[n] -= 1
                    
                    # Can it join existing  seq?
                    if (n in hyp_map) and (hyp_map[n] > 0):
                        hyp_map[n] -= 1
                        
                        # Next number it can take
                        if (n+1) in hyp_map:
                            hyp_map[n+1] += 1
                        else:
                            hyp_map[n+1] = 1
                        
                    # Create its own seq
                    else:
                        if ((n+1) in freq_map) and ((n+2) in freq_map) and (freq_map[n+1] > 0) and (freq_map[n+2] > 0):
                            freq_map[n+1] -= 1
                            freq_map[n+2] -= 1
                        else:
                            res = False
                            break

                        # Next number it can take
                        if (n+3) in hyp_map:
                            hyp_map[n+3] += 1
                        else:
                            hyp_map[n+3] = 1
    
        return res
        
