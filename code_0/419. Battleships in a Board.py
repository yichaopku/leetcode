class Solution:
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        c=0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]=='X':
                    if i-1>=0:
                        if j-1>=0:
                            if board[i-1][j]=='.' and board[i][j-1]=='.':
                                c+=1
                        else:
                            if board[i-1][j]=='.':
                                c+=1
                    else:
                        if j-1>=0:
                            if board[i][j-1]=='.':
                                c+=1
                        else:
                            c+=1
        return c