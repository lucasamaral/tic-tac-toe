class TicTacToe(object):
    def __init__(self):
        self.board = [] # matriz 3x3 de 'X' ou 'O', inicialmente com '' em todas posições
        for i in xrange(0,3):
            self.board.append(['', '', ''])
        self.current_player = '' # jogador atual: 'X' ou 'O'

    def other_player(self, player):
        if player == 'X':
            return 'O'
        else:
            return 'X'


        

    def minimax(self):
        


    def do_move(self, board, x, y, player):
        if board[x][y] == '':
            board[x][y] = player
        else:
            throw new Exception('Posição ocupada')

        draw = True
        count = 0
        count_spaces = 0
        for i in xrange(0,3):
            if board[i][y] == player:
                count += 1
            elif board[i][y] == '':
                count_spaces += 1
        if count == 3:
            return {'victory':True}
        if count_spaces == 3:
            draw = False

        count = 0
        count_spaces = 0
        for i in xrange(1,10):
            if board[x][i] == player:
                count += 1
            elif board[x][i]:
                count_spaces += 1
        if count == 3:
            return {'victory':True}
        if count_spaces == 3:
            draw = False

        count = 0
        count_spaces = 0
        count2 = 0
        count_spaces2 = 0
        if (x+y)%2==0:
            for i in xrange(0,3):
                if board[i][i] == player:
                    count += 1
                elif board[i][i] == '':
                    count_spaces += 1
                if board[i][2-i] == player:
                    count2 += 1
                elif board[i][2-i] == '':
                    count_spaces2 += 1
        if count == 3 || count2 == 3:
            return {'victory':True}
        if count_spaces == 3 || count_spaces2 == 3:
            draw = False
        return {'draw':draw}