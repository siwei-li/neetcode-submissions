class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        recursive backtracking 
        col_positions: [(0,0), (1,2), ] X
        """
        def board_output(b):
            o = []
            for x, y in b:
                row_str = "".join(['Q' if i == y else '.' for i in range(n)])
                o.append(row_str)
            return o

        def is_valid(prev_queens, nx, ny):
            for x, y in prev_queens:
                if x == nx or y == ny or nx - x == ny - y or nx + ny == x + y:
                    return False
            return True

        ans = []
        def bt(board):
            if len(board) == n:
                ans.append(board_output(board))

            r = len(board)
            for col in range(n):
                if is_valid(board, r, col):
                    bt(board + [(r, col)])
            # print(board, ans)

        bt([])
        return ans

