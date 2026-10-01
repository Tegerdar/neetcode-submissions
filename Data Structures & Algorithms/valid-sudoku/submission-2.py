class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # build new boards where each row represents box or column
        boxes_board = [["."] * 9 for _ in range(9)]
        columns_board = [["."] * 9 for _ in range(9)]
        for i, row in enumerate(board):
            for j, n in enumerate(row):
                columns_board[j][i] = n
                boxes_board[(i // 3) * 3 + (j // 3)][(i % 3) * 3 + (j % 3)] = n
        print(boxes_board)
        return (
            self._checkBoard(board) and 
            self._checkBoard(boxes_board) and 
            self._checkBoard(columns_board)
        )

    def _checkBoard(self, board: List[List[str]]) -> bool:
        # valid if each number occurs at max once in a row
        for row in board:
            seen = [False] * 9
            for n in row:
                if n != ".":
                    n = int(n)
                    if seen[n - 1]:
                        return False
                    else:
                        seen[n - 1] = True
        return True