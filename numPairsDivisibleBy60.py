class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        pass
        # (x + y) // 60 == div
        # x/60 + y/60 = div
        # 30/60 = 0.5
        
        # divmod  30
        # 20
        # 30 = 2    ans = 1
        # 20 = 2    ans = 2
        
        
        dict_ = defaultdict(int)
        ans = 0
        for i in range(len(time)):
            
            ans += dict_[60 - time[i]%60]
            
            if not time[i]%60:
                ans += dict_[time[i]%60]
            
            dict_[time[i]%60] += 1
            
        return ans
        
        
