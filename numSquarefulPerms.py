class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        
        ans = [0]
        path = []
        visited = set()
        pathVisited = set()
        
        
        @lru_cache(None)
        def dfs(curVisited):
            
            if len(path) == len(nums):
                
                if curVisited not in visited:
                    ans[0] += 1
                    visited.add(curVisited)
                    return 1
                
                else:
                    return 0
                 
            res = 0
            
            for i in range(len(nums)):
                
                if i not in pathVisited:
                    if path:
                        sqr = path[-1] + nums[i]
                        cur = floor(math.sqrt(sqr))

                        if cur**2 == sqr:
                            pathVisited.add(i)
                            path.append(nums[i])
                            res += dfs(tuple(path))
                            
                            pathVisited.remove(i)
                            path.pop()
                         


                    else:
                        pathVisited.add(i)
                        path.append(nums[i])
                        res += dfs(tuple(path))
                        pathVisited.remove(i)
                        path.pop()
                        
            return res      
        
        dfs(())
        
        return ans[0]
                        
