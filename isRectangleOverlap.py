class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:        
        if min(rec2[2], rec1[2]) > max(rec1[0],  rec2[0]) and min(rec1[3], rec2[3]) > max(rec2[1],  rec1[1]):
            return True
        return False
