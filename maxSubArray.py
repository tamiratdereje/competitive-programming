class Solution: 
    def maxSubArray(self, nums: List[int]) -> int:
        max_ = -inf
        take = 0
        
        for i in range(len(nums)):
            take = max(nums[i], nums[i] + take)
            max_ = max(max_, take)
        
        return max_
