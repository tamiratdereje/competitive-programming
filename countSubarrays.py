class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        
   
        countMax = 0
        countMin = 0
        j = 0
        
        ans = 0
        first = True
        left_over = 0
        for i in range(len(nums)):
            left_over-=1
            if nums[i] < minK:
                first, left_over = True, 0
                j = i + 1
                countMin = countMax = 0
                
            if nums[i]  > maxK :
                first, left_over = True, 0
                j = i + 1
                countMin = countMax = 0
                
            if nums[i] == minK:
                countMin += 1
                
            if nums[i] == maxK:
                + += 1
            
            if countMax > 0 and countMin > 0 and first:
                first = False
                left_over = 0
                for ind in range(i+1, len(nums)):
                    if nums[ind] > maxK or nums[ind] < minK:
                        break
                    left_over += 1
            
            while j < len(nums) and countMin > 0 and countMax > 0:
                ans += 1 + left_over
                
                if nums[j] == minK:
                    countMin -= 1
                if nums[j] == maxK:
                    countMax -= 1
                j += 1
        
        return ans
            
            
