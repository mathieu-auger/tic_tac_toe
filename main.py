

board = [" " ," " ," " ," " ," " ," " ," " ," " ," "]
# print(board)
def affichage(board):
    print(board[0], "|", board[1],  "|", board[2])
    print("------------")
    print(board[3], "|", board[4],  "|", board[5])
    print("------------")
    print(board[6], "|", board[7],  "|", board[8])

#affichage(board)

symbole_joueur1 = "X"
symbole_joueur2 = "O"

def jouer():
    joueur1 = input("Entrer le prenom du premier joueur ")
    joueur2 = input("Entrer le prenom du deuxieme joueur ")
    liste_joueurs = [joueur1, joueur2]
    print(len(board))
    
    while len(board) <= 9:
        for i in liste_joueurs:
            print("C est au tour de ", i)
            if i == joueur1:
                choice_joueur1 = int(input("Choisissez une case entre 0 et 8 "))
                while board[choice_joueur1] != " ":
                    print("Case deja occupée")
                    choice_joueur1 = int(input("Choisissez une case entre 0 et 8 "))
                    
                else:
                    board[choice_joueur1] = "X"
                    
            affichage(board)
            if i == joueur2:
                choice_joueur2 = int(input("Choisissez une case entre 0 et 8 "))
                board[choice_joueur2] = "O"
                affichage(board)

    affichage(board)

jouer()