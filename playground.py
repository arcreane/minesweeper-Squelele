import random
import os

#height=column=x
#width=row=y
#self.gridGame[int(y)][int(x)]

class Playground:
    def __init__(self, width, height, mines):
        self.width = width
        self.height = height
        self.mines = mines
        self.grid = [['0' for _ in range(width)] for _ in range(height)]
        self.gridGame = [['࿖' for _ in range(width)] for _ in range(height)]
        self.place_mines()

    def place_mines(self):
        # Code pour placer les mines aléatoirement dans la grille
        for n in range(0,self.mines):
            self.placeBomb()
        pass

    def play(self):
        game_over = False
        while not game_over:
            self.display_grid()
            # Code pour gérer les entrées du joueur et mettre à jour la grille
            action = input("Do you want to uncover a tile (U) or flag a mine (F)\n")
            if action.upper() == 'U':
                x = input("Wich tile do you want to uncover : \nenter COLUMN :")
                y = input("enter ROW :")
                if self.grid[int(y)][int(x)] == '*':
                    game_over = True
                    print("BOMB!\n you have died. Not big surprise")
                else:
                    self.gridGame[int(y)][int(x)] = ' '
                    for r in range(0, self.width-1):
                        for c in range(0, self.height-1):
                            value = self.gridGame[r][c]
                            if value == '*':
                                self.updateValues(r, c)
            elif action.upper() == 'F':
                x = input("Wich tile do you want to flag : \nenter COLUMN :")
                y = input("enter ROW :")
                self.gridGame[int(y)][int(x)] = ['⚐' for _ in y for _ in x]
                #print(self.grid)
            else:
                print("input error")


            # Vérifier les conditions de victoire ou de défaite
            if game_over == True:
                exit()
            os.system('cls')
            pass

    def display_grid(self):
        # Code pour afficher la grille actuelle
        for l in range(0, self.height):
            print("  ",l, end=' ')
        print()
        for m in range(0, self.width-1):
            print(m, self.grid[m])
        for n in range(0, self.height):
            print("  ",n, end=' ')
        print()
        for o in range(0, self.height):
            print("  ",o, end=' ')
        print()
        for p in range(0, self.width-1):
            print(p, self.gridGame[p])
        for q in range(0, self.height):
            print("  ",q, end=' ')
        print()
        pass
    def placeBomb(self):
        r = random.randint(0, (self.width-1))
        c = random.randint(0, (self.height-1))
        #print(r)
        #print(len(self.grid))
        currentRow = self.grid[r]
        if not currentRow[c] == '*':
            currentRow[c] = '*'
        else:
            self.placeBomb()

    def updateValues(self, rn, c):
        # Row above.
        if rn - 1 > -1:
            r = self.grid[rn - 1]

            if c - 1 > -1:
                if not r[c - 1] == '*':
                    r[c - 1] += 1
            if not r[c] == '*':
                r[c] += 1
            if 9 > c + 1:
                if not r[c + 1] == '*':
                    r[c + 1] += 1
        # Same row.
        r = self.grid[rn]
        if c - 1 > -1:
            if not r[c - 1] == '*':
                r[c - 1] += 1
        if 9 > c + 1:
            if not r[c + 1] == '*':
                r[c + 1] += 1
        # Row below.
        if 9 > rn + 1:
            r = self.grid[rn + 1]
            if c - 1 > -1:
                if not r[c - 1] == '*':
                    r[c - 1] += 1
            if not r[c] == '*':
                r[c] += 1
            if 9 > c + 1:
                if not r[c + 1] == '*':
                    r[c + 1] += 1


