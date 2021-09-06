import math
import random

class Player:
    def __init__(self, letter):
        # letter is X or O
        self.letter = letter

    def get_move(self, game):
        pass

# inherits from player 
class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)        # inherit attributes from parent

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8): ')
            # check value: if not return invalid, if spot is unavailable return invalid  
            try:
                val = int(square)   # first try and cast input as int i.e. if value is int
                if val not in game.available_moves():
                    raise ValueError                    # raise error if value a valid one
                valid_square = True
            except ValueError:
                print('Invalid square, Try again.')
        return val

