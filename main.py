import os
import time
from start_game import start_game
from playground import Playground
from get_player_input import get_player_input

start_game()
fieldWidth, fieldHeight, mines = get_player_input()
os.system('cls')
print("Game is gonna start.")
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
os.system('cls')

#appel du jeu et passage des caractéristique du jeu
game = Playground(fieldWidth,fieldHeight,mines)
game.play()


