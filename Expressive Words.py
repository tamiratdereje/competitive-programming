class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        
        array = []
        count = 1
        first = s[0]
        for i in range(1, len(s)):
            if s[i] == first:
                count += 1
            else:
                array.append([first, count])
                first = s[i]
                count = 1
        array.append([first, count])
        
        ans = 0
        for word in words:
            
            query = []
            count = 1
            second = word[0]
            for i in range(1, len(word)):
                if word[i] == second:
                    count += 1
                else:
                    query.append([second, count])
                    second = word[i]
                    count = 1
            query.append([second, count])
            
            if len(query) > len(array) or len(query) < len(array):
                continue
            state = True
            for i in range(len(array)):
                if array[i][0] == query[i][0]:
                    if array[i][1] < query[i][1] or (array[i][1] > query[i][1] and array[i][1] < 3):
                        state = False
                        break
                        
                else:
                    state = False
                    break
            if state:
                ans+=1
                
                
        return ans
                
