class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        rows = len(matrix)
        cols = len(matrix[0])
        
        top = 0
        right = cols - 1
        bottom = rows - 1
        left = 0

        matrix_size = rows * cols

        ans = []

        while len(ans) < matrix_size:

            # Top row
            for c in range(left, right+1):
                ans.append(matrix[top][c])
            top += 1

            # Right col
            for r in range(top, bottom+1):
                ans.append(matrix[r][right])
            right -= 1

            if len(ans) == matrix_size: break  # When cols > rows

            # Bottom row
            for c in range(right, left-1, -1):
                ans.append(matrix[bottom][c])
            bottom -= 1

            if len(ans) == matrix_size: break  # When rows > cols

            # Left col
            for r in range(bottom, top-1, -1):
                ans.append(matrix[r][left])
            left += 1

        return ans
