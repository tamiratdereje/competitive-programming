class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        array = set(nums)
        array = list(array)
        # print(array)
        if len(array) < 3:
            return max(array)
        
        for i in range(len(array)):
            array[i] = -1 * array[i]
        
        heapq.heapify(array)
        cnt = 0
        while array:
            cnt += 1
            cur = heapq.heappop(array)
            if cnt == 3:
                return cur * -1
        
