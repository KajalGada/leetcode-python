class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        is_valid = True

        for ch in s:

            if ch in ["(", "[", "{"]:
                stack.append(ch)


            elif stack and ((stack.pop() + ch) in ["()", "[]", "{}"]):
                continue

            else:
                is_valid = False
                break

        if stack:
            is_valid = False

        return is_valid
        
