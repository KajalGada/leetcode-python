class Solution:
    def isValid(self, s: str) -> bool:
        
        if (len(s)%2) == 1:
            return False
        
        stack = []
        ans = True
        
        for ch in s:
            
            if ch is ')':
                if stack and (stack[-1] == '('):
                    stack.pop()
                else:
                    ans = False
                    break
                    
            elif ch is ']':
                if stack and (stack[-1] == '['):
                    stack.pop()
                else:
                    ans = False
                    break
            
            elif ch is '}':
                if stack and (stack[-1] == '{'):
                    stack.pop()
                else:
                    ans = False
                    break
                    
            else:
                stack.append(ch)
                
        
        if stack:
            ans = False
            
        return ans
