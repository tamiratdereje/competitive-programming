class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        
        ans = [i for i in s]
        count_ = 0
        while True:
            found = False
            j = 1
            while j < len(s):
                
                if ans[j-1] + ans[j] == '01':
                    ans[j-1], ans[j] = ans[j], ans[j-1]
                    found = True
                    if j + 1 < len(s) and ans[j+1] == '1':
                        j += 1                        
                    
                j += 1
            
            # print(ans)
            if found:
                count_ += 1
            if not found:
                return count_
