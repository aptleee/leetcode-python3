class Solution:
    def generateMatrix(self, n: 'int') -> 'List[List[int]]':
        top, down, left, right = 0, n-1, 0, n-1
        x, y, dx, dy = 0, -1, 0, 1

        matrix = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n*n):
            x += dx
            y += dy
            matrix[x][y] = i+1

            if y + dy > right:
                top += 1
                dx, dy = 1, 0
            elif x + dx > down:
                right -= 1
                dx, dy = 0, -1
            elif y + dy < left:
                down -= 1
                dx, dy = -1, 0
            elif x + dy < top:
                left += 1
                dx, dy = 0, 1

        return matrix

n = 3
a = Solution()
b = a.generateMatrix(n)
print(b)