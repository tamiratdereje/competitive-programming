class Solution:
    def checkValidString(self, s: str) -> bool:
        
        # (*)*()))
        
        dict_ = {'(':1, ')':-1 }
        
        
        @lru_cache(None)
        def dfs(ind, val):
            
            if val <  0:
                return False
                
            if ind == len(s):
                return not val
            
            if s[ind] == '*':
                return dfs(ind + 1, val + 1) or dfs(ind + 1, val - 1 ) or dfs(ind + 1, val)
            else:
                return dfs(ind + 1, val + dict_[s[ind]])
        
        return dfs(0, 0)
        
            
