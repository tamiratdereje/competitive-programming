class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        answer = []
        address = []
        def backtrack(ind):
            
            if ind >= len(s):
                # check whether the it is valid so var
                if len(address) == 4:
                    answer.append(".".join(address.copy()))
                return 
            
            if len(address) >= 4:
                return 
            
            if s[ind] == '0':
                address.append('0')
                backtrack(ind + 1)
                address.pop()
            else:
                for i in range(ind, min(len(s), ind + 3)):
                    
                    if int(s[ind:i+1]) <= 255 and int(s[ind:i+1]) >= 0:
                        address.append(s[ind:i+1])
                        backtrack(i + 1)
                        address.pop()
                        
        backtrack(0)
        return answer
