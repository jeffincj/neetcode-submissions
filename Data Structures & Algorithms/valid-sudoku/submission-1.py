class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r=defaultdict(list)
        c=defaultdict(list)
        s=defaultdict(list)
        for i in range(9):
            for j in range(9):
                if board[i][j]==".":
                    continue
                if board[i][j] in r[i]:
                    return False
                r[i].append(board[i][j])

                if board[i][j] in c[j]:
                    return False
                c[j].append(board[i][j])

                if board[i][j] in s[(i//3),(j//3)]:
                    return False
                s[(i//3),(j//3)].append(board[i][j])
        return True