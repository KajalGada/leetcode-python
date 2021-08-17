class Solution:
    def countNegativesRow(self, row):
        len_row = len(row)
        count_neg = 0
        
        # All negative
        if row[0] < 0:
            count_neg = len_row
            
        # Atlease one negative (last element)
        elif row[-1] < 0:
            
            start = 0
            end = len_row - 1
            
            while start < end:
                mid = start + ((end-start)//2)
                if row[mid] >= 0:
                    start = mid + 1
                else:
                    end = mid
                    
            count_neg = len_row - end
            
        return count_neg
    
    
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        num_of_neg = 0
        rows = len(grid)
        cols = len(grid[0])
        
        for ind in range(rows-1, -1, -1):
            num_of_neg += self.countNegativesRow(grid[ind])
            
        return num_of_neg
        
