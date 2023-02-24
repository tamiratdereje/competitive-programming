class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
#         logs  :- [idi, timei]
#         and k :- 
        
#         UAM : number of unique minute for a given user
#         UAM == j  number of user
        
#         0 : 2, 5, 5
#         1 : 2, 3
        
        N = len(logs)
        ans = [0]*k
        
        dict_ = defaultdict(set)
        
        for i in range(N):
            dict_[logs[i][0]].add(logs[i][1])
        
        for ele in dict_:
            
            if len(dict_[ele]) <= k:
                ans[len(dict_[ele])-1] += 1
        
        return ans
            
