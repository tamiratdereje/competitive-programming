class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        path = []
        
        def dfs(open_, close_):
            if close_ > open_:
                return 
            
            if open_ + close_ == n*2:
                if open_ == close_:
                    ans.append("".join(path.copy()))
                
                return 
            
            path.append('(')
            dfs(open_+1, close_)
            path.pop()
            
            path.append(')')
            dfs(open_, close_ + 1)
            path.pop()
        
        dfs(0,0)
        
        return ans
