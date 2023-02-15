class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        
        letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        ans=[]
        while columnNumber>0:
            
            columnNumber=columnNumber-1
            
            ans = [letters[columnNumber%26]] + ans
            
            columnNumber=columnNumber//26
            
        return "".join(ans)
