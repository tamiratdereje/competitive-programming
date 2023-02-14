class Solution:
    def minimumDeletions(self, s: str) -> int:
        acnt = 0
        bcnt = 0
        ans = 0

        for i in range(len(s)):
            
            if s[i] == 'b':
                bcnt += 1
            
            else:
                acnt += 1
                if bcnt > 0:
                    ans = min(ans + 1, bcnt )
        
        return ans
