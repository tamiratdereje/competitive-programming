class Solution:
    def maximumSwap(self, num: int) -> int:
        max_ = num
        
        another_num = str(num)
        array = [i for i in another_num]
        changed = False
        for i in range(len(array)):
            
            if int(array[i]) == 9:
                continue
            
            for j in range(i+1, len(array)):
                
                if array[i] < array[j]:
                    array[i], array[j] = array[j], array[i]
                    max_ = max(int("".join(array)), max_)
                    array[i], array[j] = array[j], array[i]
                    changed = True
            
            if changed:
                return max_
        
        return max_
                    
                    
