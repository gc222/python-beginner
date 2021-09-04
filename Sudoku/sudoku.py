# pick an empty square
# try all numbers in that square
# if it fits, move onto next square in that row
# if it doesn't fit, use backtrack algorithm
# so go back to previous square and try another number that fits
# repeat

board = [
    [7,8,0,4,0,0,1,2,0],            # 9x9 board
    [6,0,0,0,7,5,0,0,9],            # we denote 0 as empty
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

# backtracking using recursion, base case is when board is full i.e. no 0 on board
def solve(bo):
    find = find_empty(bo)   # find_empty() returns empty slot as tuple else returns None

    # base case --> executes if board is not empty; is full
    if not find:            # runs if find = None or False
        return True         
    else:
        row, col = find

    # reaches here if is empty
    for i in range (1, 10):
        if valid(bo, i, (row, col)):    # if True, i.e. num fits slot
            bo[row][col] = i            # insert num in slot

            # recursion: reaches here to move onto next slot
            if solve(bo):
                return True

            # else: reset slot back to 0 and backtrack to previous slot
            bo[row][col] = 0
        
    return False


def valid(bo, num, pos):    # board, number given, position at
                            #                      position is a tuple(i, j)
    # check row
    # in first row, iterate over each column and check if num at given slot == num
    # i.e. are any numbers in the first row == the number inserted
    # pos[i] != i is to avoid checking the slot that is being inserted
    # we want to check every number in the first row except the slot we're inserting
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:       # bo[0][0] and 2 != 0
            return False

    # check column
    # same thing as above except reversed
    if i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # check box: iterate over each element in that box
    box_x = pos[1] // 3     # pos[1] is column (x-axis), 0 is first box, 1 is second box, 2 is third box
    box_y = pos[0] // 3     # pos[0] is row (y-axis), 0 is first box, 1 is second box, 2 is third box

    # get to actual box, we need to * 3             e.g. box (0, 2)
    for i in range(box_y * 3, box_y * 3 + 3):       # range(0, 3)
        for j in range(box_x * 3, box_x * 3 + 3):   # range(6, 9)
            if bo[i][j] == num and (i, j) != pos:   # bo[0][6], bo[0][7], bo[0][8], bo[1][6], bo[1][7]
                return False

    # reaches here if num fits
    return True


def find_empty(bo):
    for i in range(len(bo)):            # iterates over each row
        for j in range(len(bo[0])):     # iterates over each col
            if bo[i][j] == 0:           # e.g. bo[0][2] == 0 return (0, 2)
                return (i, j)           # return if empty: (row, col)       
    
    return None


def print_board(bo):
    for i in range(len(bo)):          # or basically range(9)      
        if i % 3 == 0 and i != 0:     # print horizontal line at every 4th row
            print("- - - - - - - - - - - - ")                        
        
        for j in range(len(bo[0])):     # len(bo[0]) = 9
            if j % 3 == 0 and j != 0:
                print(" | ", end = "")

            if j == 8:
                print(bo[i][j])         # at the last print where [8], it goes to next line
            else:                       # instead of like the print statement below
                print(str(bo[i][j]) + " ", end = "")


print_board(board)
solve(board)
print("\n------------------------------\n")
print_board(board)

