class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        lower, upper = min(nums), max(nums)
        cntingSort = [0]*abs(upper - lower + 1)
        
        for ele in nums:
            cntingSort[ele - lower] += 1
            
        cur = 0
        for i in range(len(cntingSort)-1,-1,-1):
            cur += cntingSort[i]
            if cur >= k:
                return lower + i
            
        return -1
        
