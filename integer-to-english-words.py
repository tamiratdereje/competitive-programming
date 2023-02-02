class Solution:
    def numberToWords(self, num: int) -> str:
    
        thousGroup = []
        
        strDigits = str(num)
        i = len(strDigits) - 1
        while i >= 0:
            cur = strDigits[i-2:i+1] if i-2 >= 0 else strDigits[:i+1]
            thousGroup.append(cur)
            i -= 3
        
        thousGroup = thousGroup[::-1]
        
        # print(thousGroup)
        under10 = {
            '0': "",'1':"One",'2':"Two",'3':"Three",'4':"Four",
            '5':"Five",  '6':"Six", '7':"Seven",  '8':"Eight", '9':"Nine",
        }
       
        twoDigit = {
            '10':"Ten", '11':"Eleven", '12':"Twelve", '13':"Thirteen", '14':"Fourteen", '15':"Fifteen",
            '16':"Sixteen", '17':"Seventeen", '18':"Eighteen", '19':"Nineteen", '1': "Ten", '2':  "Twenty",
            '3':"Thirty", '4': "Forty", '5': "Fifty", '6':"Sixty", '7': "Seventy", '8': "Eighty", '9':  "Ninety",

        }
       
        powers = { 0 : "", 1 : "Thousand", 2 : "Million", 3: "Billion", 4: "Trillion"}

        def recur(nums):
            
            if len(nums) == 0:
                return []
            
            if len(nums) == 1:
                if nums[0] == '0':  #edge case
                    return []
                else:
                    return [under10[nums[0]]]

            elif len(nums) == 2:
                if nums[0] == '0': # edge case
                    return recur(nums[1:])
                else:
                    if nums[0] == '1':
                        return [twoDigit[nums]]
                    else:
                        return [twoDigit[nums[0]]] + recur(nums[1:])

            elif len(nums) == 3:
                if nums[0] == '0': # edge cases
                    return recur(nums[1:])
                else:
                    return [under10[nums[0]], "Hundred"] + recur(nums[1:])

                
        answer = []
        for ind, thous in enumerate(thousGroup):

            changed = recur(thous)
            pow_ = powers[len(thousGroup) - ind - 1]
            if len(changed) > 0:
                answer += changed
                if pow_ != "":
                    answer.append(pow_)

        return " ".join(answer) or "Zero"
