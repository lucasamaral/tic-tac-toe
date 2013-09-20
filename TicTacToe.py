import time
import sys

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
                    if result:
                        if player == self.current_player:
                            self.board[i][j] = ' '
                            return (i,j,1)
                        else:
                            self.board[i][j] = ' '
                            return (i,j,-1)
                    analisis = self.minimax_move(self.other_player(player))
                    path_results.append((i,j,analisis[2]))
                    self.board[i][j] = ' '
        path_results = sorted(path_results, key=lambda x:x[2], reverse = True)
        if player == self.current_player:
            return path_results[0]
        else:
            return path_results[-1]

    def alfa_beta_minimax(self, player, alfa, beta):
        if self.table_full(self.board):
            return (-1,-1,0)

        cur_beta_node = (-1,-1,sys.maxint)
        cur_alfa_node = (-1,-1,-sys.maxint -1)

        if not player == self.current_player:
            for i in xrange(0,3):
                for j in xrange(0,3):
                    if self.board[i][j] == ' ':
                        result = self.do_move(i,j,player)
                        if result:
                            self.board[i][j] = ' '
                            return (i,j,-1)
                        analisis = self.alfa_beta_minimax(self.other_player(player), alfa, beta) #min(beta, cur_beta_node[2])
                        if not cur_beta_node[2] <= analisis[2]:
                            cur_beta_node = (i,j,analisis[2])
                        self.board[i][j] = ' '
                        if alfa >= cur_beta_node[2]:
                            return (i,j,cur_beta_node[2])
            return cur_beta_node
        else:
            for i in xrange(0,3):
                for j in xrange(0,3):
                    if self.board[i][j] == ' ':
                        result = self.do_move(i,j,player)
                        if result:
                            self.board[i][j] = ' '
                            return (i,j,1)
                        analisis = self.alfa_beta_minimax(self.other_player(player), alfa, beta) #max(alfa,cur_alfa_node[2])
                        if not cur_alfa_node[2] >= analisis[2]:
                            cur_alfa_node = (i,j,analisis[2])
                        self.board[i][j] = ' '
                        if cur_alfa_node[2] >= beta:
                            return (i,j,cur_alfa_node[2])
            return cur_alfa_node

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

        count = 0
        for i in xrange(0,3):
            if self.board[i][y] == player:
                count += 1
        if count == 3:
            return True

        count = 0
        for i in xrange(0,3):
            if self.board[x][i] == player:
                count += 1
        if count == 3:
            return True

        count = 0
        count2 = 0
        if (x+y)%2==0:
            for i in xrange(0,3):
                if self.board[i][i] == player:
                    count += 1
                if self.board[i][2-i] == player:
                    count2 += 1
        if count == 3 or count2 == 3:
            return True

        return False

def play_game():
    game = TicTacToe()
    game.current_player = 'X'
    result = False
    game.print_board()
    while not result:
        result = game.human_move()
        game.print_board()
        game.current_player = game.other_player(game.current_player)
        # play = game.minimax_move(game.current_player)
        play = game.alfa_beta_minimax(game.current_player, -sys.maxint-1, sys.maxint)
        print 'jogada:' + str(play)
        if play[0] == -1:
            break;
        result = game.do_move(play[0], play[1], game.current_player)
        game.current_player = game.other_player(game.current_player)
        game.print_board()

play_game()