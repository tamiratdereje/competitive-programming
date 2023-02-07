class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        temp = []
        cur_count = 0
        ans = []
        
        for i in range(len(words)):
            if cur_count + len(words[i]) + len(temp) <= maxWidth:
                cur_count += len(words[i])
                temp.append(words[i])
            else:
                if len(temp) == 1:
                    ans.append(temp[0]+ ' '*(maxWidth - cur_count))
                    
                else:                
                    left_amount = maxWidth - cur_count
                    main_division, remainder = divmod(left_amount, len(temp)-1 )
                    new_ans = []
                    for j in range(remainder):
                        temp[j] += ' '
                    ans.append((" "*main_division).join(temp))
                cur_count = len(words[i])
                temp = [words[i]]
        ans.append(' '.join(temp) + (' ' * (maxWidth - cur_count - len(temp) + 1) ))
        return ans
