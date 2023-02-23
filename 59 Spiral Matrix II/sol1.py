class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:

        row = [1]*n
        mat = []
        for _ in range(n):
            mat.append(row[:])

        i = 1

        top = 0
        bottom = n - 1
        left = 0
        right = n - 1

        n_sq = n * n

        while i <= n_sq:

            # Top
            for c in range(left, right+1):
                mat[top][c] = i
                i += 1
            top += 1

            # Right
            for r in range(top, bottom+1):
                mat[r][right] = i
                i += 1
            right -= 1

            # Checkpoint
            if i > n_sq:
                break

            # Bottom
            for c in range(right, left-1, -1):
                mat[bottom][c] = i
                i += 1
            bottom -= 1

            # Checkpoint
            if i > n_sq:
                break

            for r in range(bottom, top-1, -1):
                mat[r][left] = i
                i += 1
            left += 1

        return mat
    




