class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        # letter log -> digit logs
        # letter logs sorted by content is equal identifier then lexographically
        # digit logs remain the same
        
        letterLog = []
        digitLog = []
        
        for lo in logs:
            if lo[-1].isnumeric():
                digitLog.append(lo)
                
            else:
                cur = lo.split()
                letterLog.append((" ".join(cur[1:]), cur[0]))
        
        letterLog.sort()
        ans = [letterLog[i][1] + " " + letterLog[i][0] for i in range(len(letterLog))]
        
        ans.extend(digitLog)
        
        return ans
