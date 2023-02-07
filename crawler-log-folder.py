class Solution:
    def minOperations(self, logs: List[str]) -> int:
        cnt = 0
        
        for idx, lo in enumerate(logs):
            
            if lo[:len(lo)-1] == '..' and cnt > 0:
                cnt -= 1
                
            elif lo[:len(lo)-1] not in [ '.', '..'] :
                cnt += 1
        
        return cnt
