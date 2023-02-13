class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        
        def isValid(grid,visited,row, col, m, n):
            
            return (0<=row<m) and (0<=col<n) and ((row, col) not in visited) and (grid[row][col] == 0)
           

        m = len(grid)
        n = len(grid[0])
        visited = set()
        queue = collections.deque()
        queue.append((0,0,1))
        

        self.layer = 0
        while queue:

            direction = [[0,1],[1,0],[0,-1],[-1,0],[-1,-1],[-1,1],[1,-1],[1,1]]
            row,col,level = queue.popleft()
            if row == n-1 and col == n-1:
                return level
            for dr in direction:
                new_row, new_col = row + dr[0], col + dr[1]
                if isValid(grid,visited,new_row,new_col, m, n):
                    queue.append([new_row, new_col, level + 1])
                    visited.add((new_row, new_col))
                    if new_row == n-1 and new_col == n-1:
                        return level + 1
                
        return -1
    
