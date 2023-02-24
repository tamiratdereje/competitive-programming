class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        
        ans = 0
        
        for _ in range(100):
            for i in range(len(tickets)):

                tickets[i] -= 1

                if i == k:
                    if tickets[i] <= 0:
                        return ans + 1
                    else:
                        ans += 1
                else:
                    if tickets[i] >= 0:
                        ans += 1
        
