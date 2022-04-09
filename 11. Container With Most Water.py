class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        start = 0
        end = len(height) - 1
        ans = (end - start) * min(height[end], height[start])
        while start < end:
            if height[start] < height[end]:
                while height[start] < height[end]:
                    start += 1
                    ans = max(ans, ((end - start) * min(height[end], height[start])))
            elif height[start] > height[end]:
                while height[start] > height[end]:
                    end -= 1
                    ans = max(ans, ((end - start) * min(height[end], height[start])))
            else:
                start+=1
        return ans
