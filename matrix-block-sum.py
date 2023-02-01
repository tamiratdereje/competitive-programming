class Solution:
    def matrixBlockSum(self, matrix: List[List[int]], k: int) -> List[List[int]]:
        
         # [1,2,3]   
         # [4,5,6]
         # [7,8,9]
            
            
        self.ans = []
        m = len(matrix)
        n = len(matrix[0])
        
        for i in range(m):
            temp = [0]*n
            self.ans.append(temp)
        
        for i in range(m):
            for j in range(n):
                suma = matrix[i][j]
                suma += self.ans[i-1][j] if self.isValid(m,n,i-1,j) else 0
                suma += self.ans[i][j-1] if self.isValid(m, n, i, j-1) else 0
                suma -= self.ans[i-1][j-1] if self.isValid(m, n, i-1, j-1) else 0
                self.ans[i][j] = suma
        # print(self.ans) 
        
        
        finalAns = []
        for i in range(m):
            temp = [0]*n
            finalAns.append(temp)
        
        
        for i in range(m):
            
            for j in range(n):
                
                upperRow, upperCol =  min(m - 1, i + k), min(n - 1, j + k) 
                
                lowerRow, lowerCol =  i - k - 1, j - k - 1
                if lowerRow >= 0 and lowerCol >= 0:
                    finalAns[i][j] += self.ans[lowerRow][lowerCol]
                
                if lowerCol >= 0:
                    finalAns[i][j] -= self.ans[upperRow][lowerCol]
            
                if lowerRow >= 0:
                    finalAns[i][j] -= self.ans[lowerRow][upperCol]               
                
                finalAns[i][j] += self.ans[upperRow][upperCol]
        
        return finalAns
                
                
    
    def isValid(self,m,n,row,col):
        return 0 <= row < m and 0 <= col < n
        
