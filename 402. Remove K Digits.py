class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        if len(num)<=k:
            return "0"
        for i in num:
            while stack and eval(stack[-1]) > eval(i) and k>0:
                stack.pop()
                k -= 1
            stack.append(i)

        stack = ''.join(stack)
        stack = stack[:len(stack)-k]
        
        while len(stack)>1 and stack[0] == "0":
                 stack = stack[1:]
        return stack
