import random


"""
Custom Hangman Game Object.
@Author Afaq Anwar
@Version 02/21/2019
"""


class Hangman:
    # List of words to be used.
    word_list = ["Spiderman", "Daredevil", "Jessica Jones", "Stranger Things", "Netflix", "Tensorflow", "Python", "Keras", "Machine Learning"]
    game_over = False

    # Main Constructor
    def __init__(self):
        self.current_word = random.choice(self.word_list)
        self.current_guess = ""
        for char in self.current_word:
            if char == " ":
                self.current_guess += " "
                continue

            self.current_guess += "_"

    # Method that handles each guess.
    def guess(self, char):
        self.__error_check__(char)
        for i in range(len(self.current_word)):
            if self.current_word[i:i+1].lower() == char.lower():
                new_str = self.current_guess[:i] + self.current_word[i:i+1] + self.current_guess[i+1:]
                self.current_guess = new_str
        if self.__win_check__():
            print("\n" + "You have won!")
            self.game_over = True

    # Checks if the user input is valid.
    def __error_check__(self, char):
        if not char.isalpha():
            print("Guesses can only be letters!" + "\n")
            return
        if len(char) > 1:
            print("Can only guess one character at a time!" + "\n")
            return

    # Returns True or False depending on whether the user has fully guessed the word.
    def __win_check__(self):
        return self.current_guess == self.current_word

    # Prints the updated display
    def update_display(self):
        display_str = ""
        for char in self.current_guess:
            display_str += char + " "
        print("\n" + display_str)
