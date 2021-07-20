class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        
        res = True
        if len(nums) < 3:
            res = False
            
        else:
            
            sub = [[nums.pop(0)]]
            
            while nums:
                
                n = nums.pop(0)
                
                if sub[-1][-1] == (n-1):
                    sub[-1].append(n)
                    
                else:
                    
                    found = False
                    ind = len(sub) - 1
                    while ind >= 0:
                        if (sub[ind][-1]) == (n-1):
                            sub[ind].append(n)
                            found = True
                            break
                        ind -= 1
                            
                    if not found:
                        sub.append([n])
                        
            for each_sub in sub:
                if len(each_sub) < 3:
                    res = False
                    break
                    
            print(sub)
                
        return res
                
