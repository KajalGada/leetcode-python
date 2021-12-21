class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        
        num_occ = 0
        common_walls = 0
        
        for r in range(rows):
            for c in range(cols):
                
                if grid[r][c]:
                    num_occ += 1
                    
                    if ((c+1) < cols) and (grid[r][c+1]):
                        common_walls += 1
                        
                    if ((r+1) < rows) and (grid[r+1][c]):
                        common_walls += 1
        
        
        ans = (4 * num_occ) - (2 * common_walls)
        
        return ans
        
