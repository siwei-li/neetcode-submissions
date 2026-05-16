class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        DFS (instead of union-find)

        """
        m, n = len(grid), len(grid[0])
        dirs = ((-1,0),(1,0),(0,-1),(0,1))
        def is_valid(x, y):
            return x >= 0 and x < m and y >= 0 and y < n

        def dfs(i, j):
            grid[i][j] = 2

            for dx, dy in dirs:
                x, y = i + dx, j + dy
                if is_valid(x, y):
                    if grid[x][y] == '1':
                        dfs(x, y)
        
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    ans += 1
                    dfs(i, j)

        return ans


        