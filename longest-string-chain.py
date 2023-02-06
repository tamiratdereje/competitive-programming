class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        my_set = set(words)
        
        dp = defaultdict(int)
        
        for word in sorted(words,key=len):
            
            for i in range(len(word)):
                
                cur = word[:i] + word[i+1:]
                
                if cur in my_set:
                    
                    dp[word] = max(dp[word], dp[cur] + 1)
        
        # print(dp)
        if len(dp) > 0:
            return max(dp.values()) + 1
        
        return 1
            
        
#         @lru_cache(None)
#         def dfs(cur):
            
#             if cur not in my_set:
#                 return 0
            
#             else:
                
#                 res = 1
                
#                 for i in range(len(cur)):
#                     child = cur[:i] + cur[i+1:]
                    
#                     res = max(res, dfs(child) + 1)
                
#                 return res
                    
        
#         max_ = 1
        
#         for wo in words:
#             max_ = max(max_,  dfs(wo))
        
#         return max_
