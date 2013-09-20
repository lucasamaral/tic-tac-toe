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

    def human_move(self):
        print('Digite sua jogada na forma linha,coluna: ')
        move = input()
        x = move[0]
        y = move[1]
        return self.do_move(x, y, self.current_player)

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
        for i in xrange(1,3):
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

        for i in xrange(0,3):
            spaces_hor = 0
            for j in xrange(0,3):
                if self.board[i][j] == ' ':
                    spaces_hor += 1
            if spaces_hor == 3:
                draw = False

        for i in xrange(0,3):
            spaces_vert = 0
            for j in xrange(0,3):
                if self.board[j][i] == ' ':
                    spaces_vert += 1
            if spaces_vert == 3:
                draw = False

        return {'victory':False,'draw':draw}

def play_game():
    game = TicTacToe()
    game.current_player = 'X'
    result = {'draw':False, 'victory':False}
    game.print_board()
    while not result['draw'] and not result['victory']:
        result = game.human_move()
        game.print_board()
        print result

play_game()