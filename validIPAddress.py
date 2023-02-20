class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        
        Ip4 = queryIP.split('.')
        Ip6 = queryIP.split(':')
        
        if len(Ip4) == 4:
            
            for i in Ip4:
                if len(i) > 3:
                    return "Neither"
                
                elif not len(i) or (len(i) > 1 and i[0] == '0'):
                    return "Neither"
                
                elif not i.isnumeric():
                    return "Neither"
                
                elif int(i) > 255 or int(i) < 0:
                    return "Neither"
                
            return "IPv4"
        
        elif len(Ip6) == 8:
            all_ = ['1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','f','A', 'B', 'C', 'D', 'E', 'F']
            valid = set(all_)
            
            for i in Ip6:
                
                if len(i) > 4:
                    return "Neither"
                
                elif not len(i):
                    return "Neither"
                
                else:
                    for ele in i:
                        if ele not in valid:
                            return "Neither"
            return "IPv6"    
        
        return "Neither"
