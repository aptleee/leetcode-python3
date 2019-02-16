class Solution:
    def spiralOrder(self, matrix: 'List[List[int]]') -> 'List[int]':
        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])
        if n == 0:
            return []

        top, down, left, right = 0, m-1, 0, n-1

        x, y, dx, dy = 0, -1, 0, 1

        ret = [0] * (m*n)
        for i in range(m*n):
            x += dx
            y += dy
            ret[i] = matrix[x][y]

            if y + dy > right:
                top += 1
                dx, dy = 1, 0
            elif x + dx > down:
                right -= 1
                dx, dy = 0, -1
            elif y + dy < left:
                down -= 1
                dx, dy = -1, 0
            elif x + dx < top:
                left += 1
                dx, dy = 0, 1

        return ret
