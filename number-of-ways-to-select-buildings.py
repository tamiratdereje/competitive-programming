class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        
        heapq.heapify(nums)
        
        ans = 0
        subt = 0
        
        while nums:
            # print(nums)
            cur = heapq.heappop(nums)
            if (cur - subt) > 0:
                ans +=  1
            subt += cur - subt
        
        return ans
