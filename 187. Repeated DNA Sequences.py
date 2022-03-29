class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        ans = ["AAAAACCCCC","CCCCCAAAAA"]

        visited = set()
        
        ans = set()
        li = []
        for i in range(len(s)):
            if s[i:i+10] not in visited:
                visited.add(s[i:i+10])
                continue
            else:
                if s[i:i+10] not in ans:
                    ans.add(s[i:i+10])
                    li.append(s[i:i+10])
                  
        return li
                
