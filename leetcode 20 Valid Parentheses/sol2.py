class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s)%2:
            return False
        
        stack = []
        ans = True
        
        for char in s:
            
            if char in ['(', '[', '{']:
                stack.append(char)
                
            elif len(stack) == 0:
                ans = False
                break
                
            else:
                combo = stack[-1] + char
                print(combo)
                
                if combo in ['()', '[]', '{}']:
                    stack.pop()
                    
                else:
                    ans = False
                    break

        if stack:
            ans = False
        
        return ans
        
