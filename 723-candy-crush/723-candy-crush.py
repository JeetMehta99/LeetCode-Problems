class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        if not board:
            return board
        
        flag = True
        m = len(board)
        n = len(board[0])
        
        # check for rows
        for r in range(m):
            for c in range(n-2):
                i = abs(board[r][c])
                j = abs(board[r][c+1])
                k = abs(board[r][c+2])
                if i == j and j == k and i != 0:
                    board[r][c]   = -i
                    board[r][c+1] = -j
                    board[r][c+2] = -k
                    flag = False
                    
        # check for columns
        for c in range(n):
            for r in range(m-2):
                i = abs(board[r][c])
                j = abs(board[r+1][c])
                k = abs(board[r+2][c])
                if i == j and j == k and i != 0:
                    board[r][c]   = -i
                    board[r+1][c] = -j
                    board[r+2][c] = -k
                    flag = False
        
        # crush
        if not flag:
            for c in range(n):
                ptr = m - 1
                for r in range(ptr, -1, -1):
                    if board[r][c] > 0:
                        board[ptr][c] = board[r][c]
                        ptr -= 1
                # insert zeroes at top
                for r in range(ptr, -1, -1):
                    board[r][c] = 0
        
        return board if flag else self.candyCrush(board)
                
         
        