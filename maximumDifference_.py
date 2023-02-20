class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        
        stack = []
        ans = -1
        for i in range(len(nums)):
            
            while stack and nums[i] <= stack[-1]:
                stack.pop()
            
            stack.append(nums[i])
            if len(stack) > 1:
                ans = max(ans, stack[-1] - stack[0])
                
        return ans
