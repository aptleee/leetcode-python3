class Solution:
    def exist(self, board: 'List[List[str]]', word: 'str') -> 'bool':

        visited = {}
        def dfs(m, n, depth):
            if depth == len(word):
                return True

            if m < 0 or m == len(board) or n < 0 or n == len(board[0]) or visited.get((m, n)):
                return False

            if board[m][n] != word[depth]:
                return False

            visited[(m, n)] = True
            EXIST = dfs(m+1, n, depth+1) or dfs(m-1, n, depth+1) or dfs(m, n+1, depth+1) or dfs(m, n-1, depth+1)
            visited[(m, n)] = False
            return EXIST


        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        return False

