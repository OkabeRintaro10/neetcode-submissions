class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        h = defaultdict(list)
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                h[board[i][j]].append([i, j])

        for v in h.values():
            rows = [r for r, _ in v]
            cols = [c for _, c in v]
            boxes = [(r // 3, c // 3) for r, c in v]
            dup_row = len(rows) != len(set(rows))
            dup_col = len(cols) != len(set(cols))
            dup_box = len(boxes) != len(set(boxes))

            if dup_row or dup_col or dup_box:
                return False
        return True
            