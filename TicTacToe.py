import time

class TicTacToe(object):
    def __init__(self):
        self.board = [] # matriz 3x3 de 'X' ou 'O', inicialmente com ' ' em todas posicoes
        for i in xrange(0,3):
            self.board.append([' ', ' ', ' '])
        self.current_player = ' ' # jogador atual: 'X' ou 'O'

    def other_player(self, player):
        if player == 'X':
            return 'O'
        else:
            return 'X'

    def minimax_move(self, player):
        if self.table_full(self.board):
            return (-1,-1,0)

        path_results = []

        for i in xrange(0,3):
            for j in xrange(0,3):
                if self.board[i][j] == ' ':
                    result = self.do_move(i,j,player)
                    if result['draw']:
                        self.board[i][j] = ' '
                        return (i,j,0)
                    elif result['victory']:
                        if player == self.current_player:
                            self.board[i][j] = ' '
                            return (i,j,1)
                        else:
                            self.board[i][j] = ' '
                            return (i,j,-1)
                    analisis = self.minimax_move(self.other_player(player))
                    path_results.append((i,j,analisis[2]))
                    # self.print_board()
                    self.board[i][j] = ' '
        path_results = sorted(path_results, key=lambda x:x[2], reverse = True)
        if player == self.current_player:
            return path_results[0]
        else:
            return path_results[-1]


    def human_move(self):
        print('Digite sua jogada na forma linha,coluna: ')
        move = input()
        x = move[0]
        y = move[1]
        return self.do_move(x-1, y-1, self.current_player)

    def print_board(self):
        for line in self.board:
            print('|' + ' '.join(line) + '|')

    def table_full(self, table):
        for line in table:
            if ' ' in line:
                return False
        return True

    def do_move(self, x, y, player):
        if self.board[x][y] == ' ':
            self.board[x][y] = player
        else:
            raise Exception('Posicao ocupada')

        draw = True
        count = 0
        for i in xrange(0,3):
            if self.board[i][y] == player:
                count += 1
        if count == 3:
            return {'victory':True, 'draw':False}

        count = 0
        for i in xrange(0,3):
            if self.board[x][i] == player:
                count += 1
        if count == 3:
            return {'victory':True, 'draw':False}

        count = 0
        count2 = 0
        if (x+y)%2==0:
            for i in xrange(0,3):
                if self.board[i][i] == player:
                    count += 1
                if self.board[i][2-i] == player:
                    count2 += 1
        if count == 3 or count2 == 3:
            return {'victory':True, 'draw':False}

        return {'victory':False,'draw':False}

def play_game():
    game = TicTacToe()
    game.current_player = 'X'
    result = {'draw':False, 'victory':False}
    game.print_board()
    while not result['draw'] and not result['victory']:
        result = game.human_move()
        game.print_board()
        # time.sleep(0.5)
        game.current_player = game.other_player(game.current_player)
        play = game.minimax_move(game.current_player)
        if play[0] == -1:
            break;
        result = game.do_move(play[0], play[1], game.current_player)
        game.current_player = game.other_player(game.current_player)
        game.print_board()

play_game()