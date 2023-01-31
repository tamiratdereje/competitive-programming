class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        
        bucket = []
        for i in range(len(plantTime)):
            bucket.append((growTime[i], i))
        
        bucket.sort(reverse=True)
        largest = 0
        totalPlantTime = 0
        
        for curGrow, curInd in bucket:
            
            totalPlantTime += plantTime[curInd]
            largest = max(largest, totalPlantTime + curGrow)
        
        return largest
