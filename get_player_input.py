def get_player_input():
    #Récupération des infos du jeu
    fieldWidth = int(input("Enter field row\n"))
    fieldHeight = int(input("Enter field column\n"))
    mines = int(input("How many mines ?\n"))
    return fieldWidth, fieldHeight, mines