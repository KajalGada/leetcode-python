class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        row = [1]*n
        for _ in range(m-1):
            for c_ind in range(1, n):
                row[c_ind] += row[c_ind-1]
        
        return row[-1]
        
