class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        if len(nums) == 2:
            if nums[0]==nums[1]:
                return 1
            else:
                return 0

            
        dicOdd = {}
        dicEven ={}
        currentOddMax = 0
        currentEvenMax = 0
        evenMaxVal = 0
        oddMaxVal = 0
        
        for i in range(len(nums)):
            
            if i%2==0:
                if nums[i] not in dicEven:
                    dicEven[nums[i]] = 1
                else:
                    dicEven[nums[i]] += 1 
            else:
                if nums[i] not in dicOdd:
                    dicOdd[nums[i]] = 1
                else:
                    dicOdd[nums[i]] += 1 
                    
        sorted_dicEven= sorted(dicEven.items(), key=lambda kv: kv[1], reverse = True)
        sorted_dicOdd= sorted(dicOdd.items(), key=lambda kv: kv[1], reverse = True)
        
        oddLen = len(sorted_dicOdd)
        evenLen = len(sorted_dicEven)
        
        finalEven = 0
        finalOdd = 0
        ans = 0
  
        if sorted_dicOdd[0][0] == sorted_dicEven[0][0]:
                                    
            if oddLen >= 2 and evenLen>=2:
                if sorted_dicOdd[0][1] > sorted_dicEven[0][1]:
                    return len(nums) - max((sorted_dicEven[0][1] + sorted_dicOdd[1][1]),(sorted_dicEven[1][1] + sorted_dicOdd[0][1]))
                
                
                if sorted_dicOdd[0][1] < sorted_dicEven[0][1]:
                    return len(nums) - max((sorted_dicEven[0][1] + sorted_dicOdd[1][1]),(sorted_dicEven[1][1] + sorted_dicOdd[0][1]))
                   
                if sorted_dicOdd[1][1] >= sorted_dicEven[1][1]:
                    finalOdd = sorted_dicOdd[1][1]
                    finalEven = sorted_dicEven[0][1]
                    return len(nums) - (finalEven+finalOdd)
                    
                if sorted_dicOdd[1][1] <= sorted_dicEven[1][1]:
                    finalEven = sorted_dicEven[1][1]
                    finalOdd = sorted_dicOdd[0][1]
                    
                    return len(nums) - (finalEven+finalOdd)
            elif oddLen < 2 and evenLen < 2:
                return len(nums) - max(sorted_dicOdd[0][1] , sorted_dicEven[0][1])
            
            elif oddLen == 1:
                finalEven = sorted_dicEven[1][1]
                finalOdd = sorted_dicOdd[0][1]
                return len(nums) - (finalEven+finalOdd)
                
                
            elif evenLen == 1:
                
                finalEven = sorted_dicEven[0][1]
                finalOdd = sorted_dicOdd[1][1]
                return len(nums) - (finalEven+finalOdd)
                
        else:
            ans = len(nums) - (sorted_dicOdd[0][1] + sorted_dicEven[0][1]) 
            return ans
            
  
        
        
