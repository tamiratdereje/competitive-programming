class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = []
        for i in range(len(matrix)+1):
            temp = []
            for j in range(len(matrix[0])+1):
                temp.append(0)
            dp.append(temp)
            
        ans = 0
        for i in range(len(matrix)-1,-1,-1):
            
            for j in range(len(matrix[0])-1,-1,-1):
                
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i+1][j], dp[i+1][j+1], dp[i][j+1]) + 1
                    ans = max(dp[i][j]**2, ans)
        
        return ans
