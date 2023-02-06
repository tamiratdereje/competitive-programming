class DetectSquares:

    def __init__(self):
        self.dict_ = defaultdict(int)
        
        
    def add(self, point: List[int]) -> None:
        self.dict_[(point[0], point[1])] += 1
    
    def count(self, point: List[int]) -> int:
        
        
        ans = 0
        for key in self.dict_.keys():
            upp = (key[0], point[1])
            down = (point[0], key[1])
            
            # distance
            if abs(point[0] - key[0]) != abs(point[1] - key[1]):
                continue
                
            if key[0] == point[0] or key[1] == point[1]:
                continue
            if upp not in self.dict_ or down not in self.dict_:
                continue
                
            ans += (self.dict_[key] * self.dict_[upp] * self.dict_[down])
        
        return ans
    
        
    
# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
    
