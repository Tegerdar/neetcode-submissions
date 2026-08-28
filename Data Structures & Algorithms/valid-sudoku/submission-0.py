class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        length = 9
        box_length = 3
        boxes = [[0] * length for _ in range(length)]
        columns = [[0] * length for _ in range(length)]
        for i, row in enumerate(board):
            tmp = [0] * (length + 1)
            for j, n in enumerate(row):
                if n == ".":
                    continue
                num = int(n)
                columns[j][i] = num
                box_id = (i // 3) * 3 + (j // 3)
                pos_id = (i % 3) * 3 + (j % 3)
                boxes[box_id][pos_id] = n
                tmp[num] += 1
                if tmp[num] == 2:
                    return False
        return self.check2DListOnRepeats(boxes, length) and self.check2DListOnRepeats(columns, length)

    def check2DListOnRepeats(self, given: List[List[int]], length) -> bool:
        for i, line in enumerate(given):
            tmp = [0] * (length + 1)
            for n in line:
                if n == "." or n == 0:
                    continue
                num = int(n)
                tmp[num] += 1
                if tmp[num] == 2:
                    return False
        return True
