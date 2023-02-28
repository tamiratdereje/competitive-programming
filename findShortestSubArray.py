class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        
        dict_cnt = defaultdict(int)
        dict_ind = defaultdict(list)
        max_ = 1
        
        for ind, ele in enumerate(nums):
            dict_cnt[ele] += 1
            
            max_ = max(max_, dict_cnt[ele])
            
            if len(dict_ind[ele]) == 2:
                dict_ind[ele][1] = ind
            
            else:
                dict_ind[ele] = [ind, ind]
        
        ans = len(nums)
        for ele in dict_cnt:
            
            if dict_cnt[ele] == max_:
                ans = min(ans, dict_ind[ele][1] - dict_ind[ele][0]  + 1 )
        
        return ans
    
