class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        if rowIndex == 0:
            return [1]
        
        if rowIndex == 1:
            return [1, 1]
        
        prev_row = [1, 1]
        cur_row = []
        
        for row_num in range(2, rowIndex+1):
            
            cur_row = [1] * (row_num + 1)
            
            for c in range(1, row_num):
                cur_row[c] = prev_row[c-1] + prev_row[c]
                
            prev_row = cur_row
            
        return cur_row
        
