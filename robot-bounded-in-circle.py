class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        
        # for right =  n, e, s,w  for right (dr + 1)%4
        # if left dr == 0 dr = 3 else dr -= 1
        
                     # n    e      s     w
        direction = [(0,1),(1,0),(0,-1),(-1,0)]
        curPos = [0, 0]
        dr = 0
        for ind, direc in enumerate(instructions):
            
            if direc == 'R':
                dr = (dr + 1)%4
                
            elif direc == 'L':
                if dr == 0:
                    dr = 3
                else:
                    dr -= 1
                    
            else:
                curPos[0] += direction[dr][0]
                curPos[1] += direction[dr][1]
        
        # print(dr, curPos)
        if dr == 0 and (curPos[0],curPos[1]) != (0,0):
            return False
        
        return True
                
