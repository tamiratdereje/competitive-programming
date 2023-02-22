class Solution:
    def calculate(self, s: str) -> int:
        s = '(' + s + ')'
        
        stack = []
        
        for i in range(len(s)):
            if s[i] == ' ':
                continue
            
            if stack and s[i] == ')' and stack[-1] != '(':
                
                j = len(stack) - 1
                
                while stack and s[i] == ')' and stack[j] != '(':
                    j -= 1
                # print(stack, j)
                cur = eval("".join(stack[j+1:]))
                
                stack = stack[:j]
                stack.append(str(cur))
                
            else:
                stack.append(s[i])
        
        # print(stack)
        
        return int(stack[0])
