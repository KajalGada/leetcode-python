class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        if numRows == 1:
            return [[1]]
        
        if numRows == 2:
            return [[1], [1, 1]]
        
        res = [[1], [1, 1]]
        
        for row_num in range(2, numRows):
            
            cur_row = [1] * (row_num+1)
            
            for c in range(1, row_num):
                cur_row[c] = res[-1][c-1] + res[-1][c]
                
            res.append(cur_row)
        
        return res
        
