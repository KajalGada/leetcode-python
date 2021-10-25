class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        
        if (rows == 1) and (cols == 1):
            return 4
        
        num_island = 0
        num_common = 0
        
        # Loop through all rows and cols
        for r in range(rows-1):
            for c in range(cols-1):
                
                # If island
                if grid[r][c] == 1:
                    num_island += 1
                    # check right and down neighbour
                    num_common += grid[r+1][c]
                    num_common += grid[r][c+1]
                        
            # Last col
            if grid[r][cols-1] == 1:
                num_island += 1
                #check down neighbour
                num_common += grid[r+1][cols-1]
                    
        # Check last row
        for c in range(cols-1):
            if grid[rows-1][c] == 1:
                num_island += 1
                # Check right neighbour
                num_common += grid[rows-1][c+1]
                    
        # Check bottom right corner
        num_island += grid[rows-1][cols-1]
            
            
        return (num_island*4) - (num_common*2)
        
