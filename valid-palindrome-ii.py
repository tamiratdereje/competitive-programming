class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        i = 0
        j = len(s) - 1
        count = 1
        
        def another_pal(s, ia,ja):
            
            while ia < ja:
                if s[ia] == s[ja]:
                    ia = ia+1
                    ja = ja-1
                
                else:
                    return False
            
            return True
        
        while i < j:

            if s[i] == s[j]:
                i, j = i+1, j-1
                
            else:
                first = another_pal(s,i+1,j)
                second = another_pal(s,i,j-1)
                return first or second
                
        return True
                    
