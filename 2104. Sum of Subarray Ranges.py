class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        
        ans = 0
        for i in range(len(nums)):
            mina = nums[i]
            maxa = nums[i]
            for j in range(i+1,len(nums)):
                mina = nums[j] if nums[j] < mina else mina
                maxa = nums[j] if nums[j] > maxa else maxa
                ans += (maxa - mina)
        return ans
                
