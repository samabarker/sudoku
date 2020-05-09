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


def final_check(board):
    check_list = [1,2,3,4,5,6,7,8,9]

    for i in board:
        if sorted(i) != check_list:
            return False
    
    for i in range(len(board)):
        col_vals = []
        for j in range(len(board[i])):
            col_vals.append(board[j][i])
        if sorted(col_vals) != check_list:
            return False

    for z in range(3):
        for k in range(3):
            box_list = []
            for i in range(3):
                for j in range(3):
                    box_list.append(board[k*3 + i][z*3 + j])
            if sorted(box_list) != check_list:
                return False

    return True


def solve_puzzle(board, list_of_nums = [1,2,3,4,5,6,7,8,9]):
    if find_empty_cell(board):
        pos = find_empty_cell(board)
    else:
        return True

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
    solve_puzzle(blank_board, random_list())
    list_of_nums = random_list(80)
    to_remove = [30,40,50,60]

    for i in range(0,to_remove[level-1]):
        blank_board[list_of_nums[i] % 9][list_of_nums[i] // 9] = 0

    return blank_board


if __name__ == '__main__':
    print('Welcome to Sudoku!')
    print('--------------------')
    while True:
        get_option = input('Would you like to generate a Sudoku or solve a Sudoku? (g/s/q)')
        if get_option == 'g':
            while True:
                get_level = input('Please pick a difficulty level 1-4.')
                try:
                    if int(get_level) in range(1,5):
                        sudoku = generate_sudoku(int(get_level))
                        print('')
                        print_board(sudoku)
                        print('')
                        get_solution = input('Would you like to show the solution? (y/n)')
                        if get_solution == 'y':
                            print('')
                            solve_puzzle(sudoku)
                            print_board(sudoku)
                            print('')
                            break
                        else:
                            break
                    else:
                        print('Incorrect selection - please pick a difficulty level.')
                except:
                    print('Incorrect selection - please pick a difficulty level.')
        elif get_option == "s" :
            sudoku = []
            for i in range(0,9):
                this_list = [0,0,0,0,0,0,0,0,0]
                while True:
                    try:
                        this_row = input('Please input row ' + str(i + 1) + '. Do not separate numbers. Use 0 for unknown values.')
                        this_row_int = int(this_row)
                        if len(this_row) > 9:
                            raise Exception('Too Many Numbers')
                        for j in range(0,9):
                            this_list[j] = int(this_row[j]) 
                        break
                    except:
                        print('Incorrect input.')
                sudoku.append(this_list)
            print('')
            print_board(sudoku)
            print('')
            print('Solving...')
            print('')
            solved = solve_puzzle(sudoku)
            if solved == True:
                if final_check(sudoku):
                    print_board(sudoku)
                else:
                    print('User input was not valid - it did not follow the rules of Sudoku.')
            else:
                print('Unable to solve')
            print('')
        elif get_option == "q":
            break
        else:
            continue                