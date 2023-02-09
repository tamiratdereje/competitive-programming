class Solution:
    def reformatDate(self, date: str) -> str:
        
        
        array = date.split()
        monthes = {"Jan":'01', "Feb" : '02', "Mar" : '03', "Apr":'04', "May":'05', "Jun":'06', "Jul":'07', "Aug":'08', "Sep":'09', "Oct":'10', "Nov":'11', "Dec":'12'}
        
        ans = []
        
        ans.append(array[-1])
        ans.append(monthes[array[1]])
        
        ans.append(array[0][:len(array[0])-2])
        if len(ans[2]) == 1:
            ans[2] = '0' + ans[2]
        
        return "-".join(ans)
        
        
