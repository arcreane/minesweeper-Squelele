import random
import os
from playsound import playsound

#width=column=x
#height=row=y
#self.gridGame[int(y)][int(x)]

class Playground:
    def __init__(self, column, row, mines):
        self.column = column
        self.row = row
        self.mines = mines
        self.grid = [[0 for _ in range(row)] for _ in range(column)]
        self.gridGame = [['࿖' for _ in range(row)] for _ in range(column)]
        self.place_mines()

    def place_mines(self):
        # Code pour placer les mines aléatoirement dans la grille
        for n in range(0,self.mines):
            self.placeBomb()
        pass

    def play(self):
        game_over = False
        flags_correct = 0
        while not game_over:
            self.display_grid()
            # Code pour gérer les entrées du joueur et mettre à jour la grille
            action = input("Do you want to uncover a tile (U) or flag a mine (F)\n")
            if action.upper() == 'U':
                x = input("Wich tile do you want to uncover : \nenter COLUMN :")
                y = input("enter ROW :")
                if self.grid[int(y)][int(x)] == '*':
                    game_over = True
                    print("BOMB!\n you are dead. Not big surprise")
                    playsound('./sound.mp3')
                    print('playing sound using playsound\n Game ended miserably')

                else:
                    if self.gridGame[int(y)][int(x)] == '࿖':
                        self.gridGame[int(y)][int(x)] = ' '
                        self.updateValuesGrid(int(y), int(x))

            elif action.upper() == 'F':
                x = input("Wich tile do you want to flag : \nenter COLUMN :")
                y = input("enter ROW :")
                self.gridGame[int(y)][int(x)] = '⚐'
            else:
                print("input error")

            if self.grid[int(y)][int(x)] == '*' and self.gridGame[int(y)][int(x)] == '⚐':
                flags_correct += 1

            if flags_correct == self.mines:
                game_over = True
                print("Victory!\n you played well. Nice job")
                playsound('./vsound.mp3')
                print('playing sound using playsound')
                print("Félicitations ! Vous avez correctement drapeauté toutes les mines. Vous avez gagné !")

            # Vérifier les conditions de victoire ou de défaite
            if game_over == True:
                exit()
            os.system('cls')
            pass

    def display_grid(self):
        # Code pour afficher la SOLUTION
        # Affichez l'en-tête des colonnes (numéro de colonne)
        print("   ", end='')
        for j in range(self.row):
            print(f"{j:2}", end=' ')
        print()  # Nouvelle ligne

        for o in range(self.column):
            # Affichez le numéro de ligne
            print(f"{o:2} ", end='')

            # Affichez le contenu de chaque case
            for p in range(self.row):
                cell_content = self.grid[o][p]
                print(f"{cell_content:2}", end=' ')
            print()  # Nouvelle ligne
        # Affichez l'en-tête des colonnes (numéro de colonne)
        print("   ", end='')
        for l in range(self.row):
            print(f"{l:2}", end=' ')
        print()  # Nouvelle ligne

        for m in range(self.column):
            # Affichez le numéro de ligne
            print(f"{m:2} ", end='')

            # Affichez le contenu de chaque case
            for n in range(self.row):
                cell_content = self.gridGame[m][n]
                print(f"{cell_content:2}", end=' ')
            print()  # Nouvelle ligne
        pass
    def placeBomb(self):
        r = random.randint(0, (self.column-1))
        c = random.randint(0, (self.row-1))
        #print(r)
        #print(len(self.grid))
        currentRow = self.grid[r]
        if not currentRow[c] == '*':
            currentRow[c] = '*'
            self.updateValuesMines(r,c)
        else:
            self.placeBomb()

    def updateValuesMines(self, rowNumber, columnNumber):
        # Row above
        if rowNumber - 1 > -1:
            r = self.grid[rowNumber - 1]
            if columnNumber - 1 > -1 and r[columnNumber - 1] != '*':
                self.grid[rowNumber - 1][int(columnNumber - 1)] += 1
            if r[columnNumber] != '*':
                self.grid[rowNumber - 1][columnNumber] += 1
            if self.column > columnNumber + 1 and r[columnNumber + 1] != '*':
                self.grid[rowNumber - 1][columnNumber + 1] += 1

        # Same row
        r = self.grid[rowNumber]
        if columnNumber - 1 > -1 and r[columnNumber - 1] != '*':
            self.grid[int(rowNumber)][columnNumber - 1] += 1
        if self.column > columnNumber + 1 and r[columnNumber + 1] != '*':
            self.grid[int(rowNumber)][columnNumber + 1] += 1

        # Row below
        if self.row > rowNumber + 1:
            r = self.grid[rowNumber + 1]
            if columnNumber - 1 > -1 and r[columnNumber - 1] != '*':
                self.grid[rowNumber + 1][columnNumber - 1] += 1
            if r[columnNumber] != '*':
                self.grid[rowNumber + 1][columnNumber] += 1
            if self.column > columnNumber + 1 and r[columnNumber + 1] != '*':
                self.grid[rowNumber + 1][columnNumber + 1] += 1

    def updateValuesGrid(self, row, column):
        if self.gridGame[row][column] == ' ' or self.gridGame[row][column] == '࿖':
            self.gridGame[row][column] = self.grid[row][column]
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if 0 <= row+dr < self.row and 0 <= column+dc < self.column:
                        if self.grid[row + dr][ column + dc] != '*':#tant que c'est une mine on laisse caché
                           self.gridGame[row + dr][column + dc] = self.grid[row + dr][column + dc]
                        if self.grid[row + dr][ column + dc] == 0:
                            for dr2 in [-1, 0, 1]:
                                for dc2 in [-1, 0, 1]:
                                    if 0 <= row + dr+dr2 < self.row and 0 <= column + dc+dc2 < self.column:
                                        if self.grid[row + dr + dr2][column + dc + dc2] != '*':  # tant que c'est une mine on laisse caché
                                            self.gridGame[row + dr + dr2][column + dc + dc2] = self.grid[row + dr + dr2][column + dc + dc2]




