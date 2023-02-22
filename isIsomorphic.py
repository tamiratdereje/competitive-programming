class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dicta = {} 
        dictb = {}
        for i in range(len(s)):
            if s[i] not in dicta and t[i] not in dictb:
                dicta[s[i]] = t[i]
                dictb[t[i]] = s[i]
            elif s[i] in dicta and t[i] not in dictb:
                return False
            elif s[i] not in dicta and t[i] in dictb:
                return False
            else:
                if dicta[s[i]] != t[i] or dictb[t[i]] != s[i]:
                    return False
        return True
