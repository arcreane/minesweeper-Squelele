def get_player_input():
    #Récupération des infos du jeu
    fieldRow = int(input("Enter field row\n"))
    fieldColumn = int(input("Enter field column\n"))
    mines = int(input("How many mines ?\n"))
    while mines > fieldRow * fieldColumn:
        print("Too much!")
        mines = int(input("How many mines ?\n"))
    return fieldColumn, fieldRow, mines
def get_player_input_action():
    # Récupération du choix d'action
   return input("Do you want to uncover a tile (U) or flag a mine (F)\n")

def get_player_input_gridXY():
    # Récupération des axes pour le positionnement dans la grid
    x = input("enter COLUMN :")
    y = input("enter ROW :")
    return x,y