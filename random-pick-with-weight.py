class Solution:

    def __init__(self, w: List[int]):
        
        self.w = [w[0]]
        
        for i in range(1,len(w)):
            self.w.append(self.w[i - 1] +  w[i])
        
        
    def pickIndex(self) -> int:
        choosed = random.randint(1,self.w[-1])
        
        
        left, right = 0,  len(self.w)-1
        
        while left <= right:
            
            mid = left + (right - left)//2
            if self.w[mid] == choosed:
                return mid
            elif self.w[mid] < choosed:
                left = mid + 1
            else:
                right = mid - 1
        
        return left
        
# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
