class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:       
        
        N = len(ages)
        team = [(ages[i], scores[i]) for i in range(N)]
        team.sort()
        ans = 0
        
        dp = [0] * N
        for i in range(N):
            dp[i] = team[i][1]
            for j in range(i):
                
                if team[i][1] >= team[j][1]:
                    
                    dp[i] = max(dp[i], dp[j] + team[i][1])
            ans = max(ans, dp[i])
        
        return ans
