class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:

        ans = 0
        rows = len(grid)
        cols = len(grid[0])

        row_max = []
        col_max = []

        for row in grid:
            row_max.append(max(row))

        columns = list(zip(*grid))
        
        for col in columns:
            col_max.append(max(col))

        for r in range(rows):
            for c in range(cols):
                r_max = row_max[r]
                c_max = col_max[c]
                min_max = min(r_max, c_max)
                ans += (min_max - grid[r][c])

        return ans
