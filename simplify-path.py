class Solution:
    def simplifyPath(self, path: str) -> str:
        li = list(path.split('/'))
        stack = []
        for path in li:
            if path == "":
                continue
                
            if path != ".." and path != ".":
                stack.append(path)
                continue
                
            if stack and path == "..":
                stack.pop()
                
        
        if len(stack) == 0:
            return "/"
        ans = ['/']
        for i in stack:
            ans.append(i)
            ans.append('/')
        ans.pop()
        return "".join(ans)
