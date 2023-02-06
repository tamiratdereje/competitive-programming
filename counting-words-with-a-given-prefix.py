class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        N = len(words)
        prLen = len(pref)
        ans = 0
        
        for i in range(N):
            if len(pref) > len(words[i]):
                continue
                
            found = True
            for j in range(prLen):
                
                if pref[j] != words[i][j]:
                    found = False
                    break
            
            if found:
                ans += 1
        
        return ans
