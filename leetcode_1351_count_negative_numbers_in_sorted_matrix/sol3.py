class Solution:
    
    def countNegRow(self, row, start, len_row):

        end = len_row - 1
        while start < end:
            mid = start + ((end-start)//2)
            if row[mid] < 0:
                end = mid
            else:
                start = mid+1
                
        return (len_row - start), start
    
    
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        count = 0
        start_ind = 0
        len_row = len(grid[0])
        
        while grid and grid[-1][-1] < 0:
            row = grid.pop()
            count_row, start_ind = self.countNegRow(row, start_ind, len_row)
            count += count_row
            
        return count
        
