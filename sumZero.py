class Solution:
    def sumZero(self, n: int) -> List[int]:
        
        # return [-3, -2, -1, 0, 1, 2, 3]
        
        answer = [] if n%2 == 0 else [0]
        
        for i in range(1, n//2 + 1 ):
            answer.append(i)
            answer.append(-i)
            
        return answer
