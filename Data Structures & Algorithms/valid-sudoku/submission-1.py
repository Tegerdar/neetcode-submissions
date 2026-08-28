class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        length = 9
        rows = [set() for _ in range(length)]
        columns = [set() for _ in range(length)]
        boxes = [set() for _ in range(length)]
        for i in range(length):
            for j in range(length):
                n = board[i][j]
                if n == ".":
                    continue
                b = (i // 3) * 3 + (j // 3)
                if n in rows[i] or n in columns[j] or n in boxes[b]:
                    return False
                rows[i].add(n)
                columns[j].add(n)
                boxes[b].add(n)
        return True