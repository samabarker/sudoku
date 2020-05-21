import random
from os import system, name


# Function to clear the screen
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


# Word list to pass to game
words = ['hello', 'television', 'computer', 'mouse', 'keyboard', 'piano', 'cabinet', 'wardrobe', 'frame', 'house',
         'home', 'picture', 'mug', 'kettle', 'table', 'pasta', 'pizza', 'tomato', 'banana', 'couch', 'flower',
         'butterfly', 'vase', 'wedding', 'walking', 'running', 'diet', 'soda']


# Game class holding information and methods
class Game:
    # Initialise the function - list for correct guesses, list for incorrect guesses, and list to hold current word
    def __init__(self, words):
        self.correct_guesses = []
        self.incorrect_guesses = []
        self.words = words

    # Class variable list holding pictures for the game
    hung_men = ['''
                     ---
                    |   | 
                    |    
                    |   
                    |    
                ____|____
                ''',
                '''
                     ---
                    |   | 
                    |    o
                    |   
                    |    
                ____|____
                ''',
                '''
                     ---
                    |   | 
                    |    o
                    |    |
                    |    
                ____|____
                ''',
                '''
                     ---
                    |   | 
                    |    o
                    |   /|
                    |   
                ____|____
                ''',
                '''
                     ---
                    |   | 
                    |    o
                    |   /|\\
                    |    
                ____|____
                ''',
                '''
                     ---
                    |   | 
                    |    o
                    |   /|\\
                    |   /
                ____|____
                ''',
                '''
                     ---
                    |   | 
                    |    o
                    |   /|\\
                    |   / \\
                ____|____
                ''']

    # Function to get random word from the list
    def get_random_word(self):
        list_len = len(self.words)
        word = words[(random.randint(0,list_len - 1))]
        self.word = word

    # Function to return current progress (uses _ for unguessed letters)
    def get_current_progress(self):
        progress = ''
        for i in self.word:
            if i in self.correct_guesses:
                progress = progress + i
            else:
                progress = progress + '_'
        return progress

    # Function that takes users guess and checks if it is correct or incorrect. Puts guess in relevent list
    def checker(self, choice):
        if len(choice) == 1 and choice.isalpha():
            if choice in self.correct_guesses or choice in self.incorrect_guesses:
                pass
            elif choice in self.word:
                self.correct_guesses.append(choice)
            else:
                self.incorrect_guesses.append(choice)

    # Function to print out current progress. Also prints title
    def print_current(self):
        print('Welcome to Hangman!')
        print('--------------------')
        print(self.hung_men[len(self.incorrect_guesses)])
        print('Word: ', end = '')
        print(self.get_current_progress(), end = '')
        print(' (' + str(len(self.word)) + ' letters)')
        print('Correct Guesses: ', end = '')
        print(self.correct_guesses)
        print('Incorrect Guesses: ', end='')
        print(self.incorrect_guesses)
        print('')

    # Run function - gets user input and calls other relevent functions
    def run(self):
        self.get_random_word()
        while True:
            clear()
            if len(self.incorrect_guesses) == 6:
                self.print_current()
                print('')
                print('YOU LOSE!')
                print('Word was: ', end = '')
                print(self.word)
                break
            elif self.get_current_progress() == self.word:
                self.print_current()
                print('')
                print('YOU WIN!')
                print('You guessed the word: ' + self.word)
                break
            else:
                self.print_current()
                choice = input("Please choose a letter: ").lower()
                self.checker(choice)


# Check if file being run is this file
if __name__ == '__main__':
    Game(words).run()