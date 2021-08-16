class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        res = []
        rows = len(mat)
        cols = len(mat[0])
        
        if (rows * cols) != (r*c):
            res = mat
        
        elif (r == 1):
            for row in mat:
                res += row
            res = [res]
            
        elif c == 1:
            for row in mat:
                for num in row:
                    res.append([num])
                
        else:
            cur_row = []
            for row in mat:
                cur_row += row
                while c <= len(cur_row):
                    res.append(cur_row[0:c])
                    cur_row = cur_row[c:]
                    
        # print(res)
        return res
            
