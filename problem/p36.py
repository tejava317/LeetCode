class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for i in range(9):
            s = set()
            for j in range(9):
                if board[i][j] in s:
                    return False
                else:
                    if not board[i][j] == '.':
                        s.add(board[i][j])
        
        for i in range(9):
            s = set()
            for j in range(9):
                if board[j][i] in s:
                    return False
                else:
                    if not board[j][i] == '.':
                        s.add(board[j][i])
        
        for h in range(0, 9, 3):
            for w in range(0, 9, 3):
                s = set()
                for i in range(3):
                    for j in range(3):
                        if board[i + h][j + w] in s:
                            return False
                        else:
                            if not board[i + h][j + w] == '.':
                                s.add(board[i + h][j + w])
        
        return True