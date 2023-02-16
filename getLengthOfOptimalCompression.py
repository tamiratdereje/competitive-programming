class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        path = []
        first, count = s[0], 1
        
        for i in range(1,len(s)):
            if first!=s[i]:
                path.append((first, count))
                first,count = s[i], 1
                continue
            count += 1
        path.append((first, count))

        @lru_cache(None)
        def dfs(ind = 0, ope = k, lst_ch = '*', count = 1):
            if ind == len(path):
                print(1 + (0 if count == 1 else len(str(count))))
                return 1 + (0 if count == 1 else len(str(count)))
            
            c_ch, c_cnt = path[ind]
            best = inf
            
            # same char 
            if c_ch == lst_ch:
                for i in range(min(ope, c_cnt) + 1):
                    res = dfs(ind + 1, ope - i, c_ch, count + c_cnt - i)
                    best = min(best, res)
             
            # mulu statefa
            if c_cnt <= ope:
                    res = dfs(ind + 1, ope - c_cnt, lst_ch, count)
                    best = min(best, res)
                    
            # diff char
            if c_ch != lst_ch:
                # copress yedrown 
                compp = 1 + (0 if count == 1 else len(str(count)))
                
                for i in range(min(ope, c_cnt) + 1):
                    res = dfs(ind + 1, ope - i, c_ch, c_cnt - i)
                    best = min(best, res + compp)
                
            
            return best
        
        return dfs() - 1
