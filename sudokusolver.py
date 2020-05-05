import random


def random_list(num=9):
    list_nums = []
    while True:
        if len(list_nums) == num:
            return list_nums
        n = random.randint(1,num)
        if n in list_nums:
            continue
        else:
            list_nums.append(n)


def draw_board(n=9):
    board = []
    for i in range(n):
        board.append([])
        for j in range(n):
            board[i].append(0)
    return board


def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print('---------------------')
        for j in range(len(board[i])):
            if j % 3 == 0 and j != 0:
                print('| ', end = '')
            if board[i][j] != 0:
                print(board[i][j], end = ' ')
            else:
                print('?', end = ' ')
        print('')

def find_empty_cell(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return [i,j]
    return False


def check_valid(pos, num, board):
    row_val = pos[0]
    col_val = pos[1]

    if num in board[row_val]:
        return False

    for i in range(len(board)):
        if board[i][col_val] == num:
            return False

    box_row = row_val // 3
    box_col = col_val // 3

    for i in range(3):
        for j in range(3):
            if board[box_row * 3 + i][box_col * 3 + j] == num:
                return False
    return True


def solve_puzzle(board):
    if find_empty_cell(board):
        pos = find_empty_cell(board)
    else:
        return True

    list_of_nums = random_list()

    for i in list_of_nums:
        if check_valid(pos, i, board):
            row_val = pos[0]
            col_val = pos[1]
            board[row_val][col_val] = i
            if solve_puzzle(board):
                return True
            board[row_val][col_val] = 0
    return False


def generate_sudoku(level):
    blank_board = draw_board()
    solve_puzzle(blank_board)
    list_of_nums = random_list(80)
    to_remove = [30,40,50,60]

    for i in range(0,to_remove[level-1]):
        blank_board[list_of_nums[i] % 9][list_of_nums[i] // 9] = 0

    return blank_board


# Sample Sudoku
sudoku1 = [[0,0,3,0,0,0,0,0,0],
          [5,8,0,2,0,0,3,0,9],
          [2,0,0,4,0,5,8,7,1],
          [3,7,0,0,1,0,5,9,0],
          [8,0,0,7,4,0,1,3,0],
          [0,2,9,0,0,8,0,0,0],
          [6,0,0,1,0,3,4,0,7],
          [4,0,2,0,6,0,0,0,0],
          [0,0,0,5,2,4,6,8,0]]


# SOLVE (UNCOMMENT BELOW)
#solved = solve_puzzle(sudoku1)
#if solved == True:
#    print_board(sudoku1)
#else:
#    print('Unable to solve')


# GENERATE
level = 4        # levels 1-4, 1 = easy, 4 = hard
sudoku2 = generate_sudoku(level)
print_board(sudoku2)
print('')
print('')
solve_puzzle(sudoku2)
print_board(sudoku2)