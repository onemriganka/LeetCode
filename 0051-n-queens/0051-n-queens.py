class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        res = []
        board = [['.'] * n for _ in range(n)]
        cols = set()
        pos_diagonals = set()  # (r + c)
        neg_diagonals = set()  # (r - c)

        def backtrack(r):
            if r == n:
                # Convert board to list of strings
                solution = [''.join(row) for row in board]
                res.append(solution)
                return

            for c in range(n):
                if c in cols or (r + c) in pos_diagonals or (r - c) in neg_diagonals:
                    continue  # not safe

                # Place queen
                board[r][c] = 'Q'
                cols.add(c)
                pos_diagonals.add(r + c)
                neg_diagonals.add(r - c)

                backtrack(r + 1)

                # Remove queen (backtrack)
                board[r][c] = '.'
                cols.remove(c)
                pos_diagonals.remove(r + c)
                neg_diagonals.remove(r - c)

        backtrack(0)
        return res

# Time Complexity: O(N!) 
# Space Complexity: O(N^2)
 
        