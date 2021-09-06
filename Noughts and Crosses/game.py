import time
from player import HumanPlayer, RandomComputerPlayer

class NoughtCrosses:
    def __init__(self):
        self.board = [' ' for _ in range(9)]    # [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.current_winner = None          # keep track of winner

    
    def print_board(self):
        for row in [self.board[i * 3:(i + 1) * 3] for i in range(3)]: # represents which row
            print('| ' + ' | '.join(row) + ' |')


            # 0 + 1 = 1     * 3 = 3     0: 3    indices [0 1 2] will be first row
            # 1 + 1 = 2     * 3 = 6     3: 6    indices [3 4 5] will be second row
            # 2 + 1 = 3     * 3 = 9     6: 9    indices [6 7 8] will be third row

    @staticmethod
    def print_board_nums():     # 0 | 1 | 2 etc (tells us what number corresponds to what box)
        number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')
    
    def available_moves(self):
        # return [i for i, spot in enumerate(self.board) if spot == ' ']
        moves = []
        for (i, spot) in enumerate(self.board):
            #['x', 'x', 'o'] --> [(0, 'x'), (1, 'x'), (2, 'o')]
            if spot == ' ':
                moves.append(i)     # i is the index e.g. append(1) to inform index 1 is available
        return moves

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')    # count empty squares

    def make_move(self, square, letter):
        # if valid move, then make move (assign square to letter)
        # then return true, else return false
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # winner if 3 in a row anywhere
        # check row
        row_ind = square // 3
        row = self.board[row_ind * 3 : (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True

        # check column
        col_ind = square % 3
        column = [self.board[col_ind + i * 3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        
        # check diagonals   only if square is an even number (0, 2, 4, 6, 8)
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]  # left to right diagonal
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True
        
        # if all these fail
        return False


def play(game, x_player, o_player, print_game=True):
    if print_game:  # if true
        game.print_board_nums()
    
    letter = 'X' # starting letter

    # get the move from the appropriate player
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print('')

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter

            # switches player --> alternate letters after move is made
            letter = 'O' if letter == 'X' else 'X'
        time.sleep(0.8)
    if print_game:
        print('It\'s a tie!')


if __name__ == '__main__':          # body of code only runs if this file is executed directly
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    t = NoughtCrosses()
    play(t, x_player, o_player, print_game=True)