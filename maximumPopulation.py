class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        
        prefix = [0]*101
        
        for first, second in logs:
            
            prefix[first - 1950] += 1
            
            prefix[second - 1950] -= 1
        
        for i in range(1, 101):
            prefix[i] += prefix[i-1]
    
        ans = 1950
        max_ = 0
        
        for i in range(101):
            if prefix[i] > max_ :
                ans = i + 1950
                max_ = prefix[i]
        
        return ans
