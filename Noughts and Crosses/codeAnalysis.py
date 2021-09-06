# class NoughtCrosses:
#     def __init__(self):
#         self.board = [' ' for _ in range(9)]   

#     def print_board(self):
#         for row in [self.board[i * 3:(i + 1)] * 3 for i in range(3)]: 
#             print('| ' + ' | '.join(row) + ' |')

# x = NoughtCrosses()
# x.print_board 


board = [' ' for _ in range(9)] # [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

for row in [board[i * 3:(i + 1) * 3] for i in range(3)]:    
    print('| ' + ' | '.join(row) + ' |')                    
                                                            
        # 0 + 1 = 1     * 3 = 3     0: 3    indices [0 1 2] will be first row
        # 1 + 1 = 2     * 3 = 6     3: 6    indices [3 4 5] will be second row
        # 2 + 1 = 3     * 3 = 9     6: 9    indices [6 7 8] will be third row

# for row in [board[0: 3]] --> |   |   |   |
# for row in [board[3: 6]] --> |   |   |   |
# for row in [board[6: 9]] --> |   |   |   |
