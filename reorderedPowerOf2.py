class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        
        for i in list(itertools.permutations(str(n))): 
            if i[0]!='0' and bin(int("".join(i))).count('1') == 1:
                return True
        return False   
