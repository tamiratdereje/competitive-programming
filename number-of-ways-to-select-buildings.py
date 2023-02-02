class Solution:
    def numberOfWays(self, s: str) -> int:
        dp = {'0' : 0, '1' : 0, '01': 0, '10':0, '010':0, '101':0}
        
        for i in range(len(s)):
            if s[i] == '0':
                dp['10'] += dp['1']
                dp['0'] += 1
                dp['010'] += dp['01'] 
                
            else:
                dp['01'] += dp['0']
                dp['1'] += 1
                dp['101'] += dp['10']
        
        return dp['101'] + dp['010']
    
            
        
        @lru_cache(None)
        def dfs(prev, ind, count_):
            
            if count_ == 3:
                return 1
            
            if ind >= len(s):
                return 0
            
            res = 0
            
            res += dfs(prev, ind + 1, count_)
            if prev != s[ind]:
                res += dfs(s[ind], ind + 1, count_ + 1)
                        
            return res
        
        # return dfs(-1, 0, 0)
