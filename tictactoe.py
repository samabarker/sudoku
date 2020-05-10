import random
from os import system, name


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


class Game:
    def __init__(self):
        self.board = [[0,0,0], [0,0,0], [0,0,0]]
        self.ref_board = [[1,2,3], [4,5,6], [7,8,9]]
        self.positions = [[0,0], [0,1], [0,2], [1,0], [1,1], [1,2], [2,0], [2,1], [2,2]]

    def print_board(self,board):
        print('')
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 0:
                    var = ' '
                elif board[i][j] == 'P':
                    var = 'X'
                elif board[i][j] == 'C':
                    var = 'O'
                else:
                    var = board[i][j]
                print(var, end = '')
                if j / 2 != 1:
                    print(' | ', end = '')
            print('')
            if i / 2 != 1:
                print('----------')
        print('')

    def find_empty(self):
        if not self.check_board():
            while True:
                pos = random.randint(0,8)
                row_val = self.positions[pos][0]
                col_val = self.positions[pos][1]
                if self.board[row_val][col_val] == 0:
                    self.board[row_val][col_val] = 'C'
                    break

    def check_valid(self, choice):
        if choice.isnumeric():
            choice = int(choice)
            if choice in range(10):
                board_ref = self.positions[choice-1]
                if self.board[board_ref[0]][board_ref[1]] == 0:
                    self.board[board_ref[0]][board_ref[1]] = 'P'
                    return True

    def print_current(self):
        print('Welcome to Tic Tac Toe!')
        print('-----------------------')
        self.print_board(self.ref_board)
        print('Current Progress:')
        self.print_board(self.board)

    def check_board(self):
        if (self.board[0][0] == self.board[0][1] == self.board[0][2]) and self.board[0][0] != 0:
            if self.board[0][0] == 'C':
                print('Computer Wins!')
            else:
                print('You Win!')
            return True
        elif (self.board[1][0] == self.board[1][1] == self.board[1][2]) and self.board[1][0] != 0:
            if self.board[1][0] == 'C':
                print('Computer Wins!')
            else:
                print('You Win!')
            return True
        elif (self.board[2][0] == self.board[2][1] == self.board[2][2]) and self.board[2][0] != 0:
            if self.board[2][0] == 'C':
                print('Computer Wins!')
            else:
                print('You Win!')
            return True
        elif (self.board[0][0] == self.board[1][0] == self.board[2][0]) and self.board[0][0] != 0:
            if self.board[0][0] == 'C':
                print('Computer Wins!')
            else:
                print('You Win!')
            return True
        elif (self.board[0][1] == self.board[1][1] == self.board[2][1]) and self.board[0][1] != 0:
            if self.board[0][1] == 'C':
                print('Computer Wins!')
            else:
                print('You Win!')
            return True
        elif (self.board[0][2] == self.board[1][2] == self.board[2][2]) and self.board[0][2] != 0:
            if self.board[0][2] == 'C':
                print('Computer Wins!')
            else:
                print('You Win!')
            return True
        elif (self.board[0][0] == self.board[1][1] == self.board[2][2]) and self.board[0][0] != 0:
            if self.board[0][0] == 'C':
                print('Computer Wins!')
            else:
                print('You Win!')
            return True
        elif (self.board[0][2] == self.board[1][1] == self.board[2][0]) and self.board[0][2] != 0:
            if self.board[0][2] == 'C':
                print('Computer Wins!')
            else:
                print('You Win!')
            return True
        elif 0 not in self.board[0] and 0 not in self.board[1] and 0 not in self.board[2]:
            print('Noone Wins...')
            return True
        return False

    def run(self):
        while True:
            clear()
            self.print_current()
            if self.check_board():
                break
            else:
                choice = input('Where would you like to play?')
                if self.check_valid(choice):
                    self.find_empty()


if __name__ == '__main__':
    Game().run()

 
