def get_player_input():
    #Récupération des infos du jeu
    fieldRow = int(input("Enter field row\n"))
    fieldColumn = int(input("Enter field column\n"))
    mines = int(input("How many mines ?\n"))
    while mines > fieldRow * fieldColumn:
        print("Too much!")
        mines = int(input("How many mines ?\n"))
    return fieldColumn, fieldRow, mines