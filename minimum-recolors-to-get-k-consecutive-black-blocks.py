class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
        colorCnt = Counter(blocks[:k])
        left = 0
        
        ans = colorCnt['W']
        
        for right in range(k, len(blocks)):
            
            if blocks[right] == 'W':
                colorCnt['W'] += 1
            
            if blocks[left] == 'W':
                colorCnt['W'] -= 1
            
            left += 1
            ans = min(ans, colorCnt['W'])
    
        return ans
