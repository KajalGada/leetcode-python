class Solution:
    def simplifyPath(self, path: str) -> str:

        dirs = path.split("/")
        stack = []

        for d in dirs:
            if d and d != ".":
                if d == "..":
                    if stack:
                        stack.pop()
                else:
                    stack.append(d)

        new_path = "/" + "/".join(stack)

        return new_path
