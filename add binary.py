class Solution:
    def addBinary(self, a: str, b: str) -> str:
        rem = 0
        result = ''

        a = list(a)
        b = list(b)

        while a or b or rem:
            if a:
                rem += int(a.pop())
            if b:
                rem += int(b.pop())
            
            if rem == 0 or rem == 2:
                result += '0'
            else:
                result += '1'
                
            rem //= 2

        return result[::-1]
