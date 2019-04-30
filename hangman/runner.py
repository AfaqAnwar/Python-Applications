from hangman.game import Hangman

"""
Hangman Runner
@Author Afaq Anwar
@Version 02/21/2019
"""
current_game = Hangman()
print("Welcome to Hangman!" + "\n" + "Attempt to guess the word!")
current_game.update_display()

while not current_game.game_over:
    current_game.guess(input("Type..."))
    current_game.update_display()
