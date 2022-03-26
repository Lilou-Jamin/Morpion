def afficher_grille(grille): #Création de la grille 3x3
    for i in range(0,3):
        print(grille[i])

# Fonction qui teste si un joueur a gagné. Si il y a match nul et si il y a une case de libre.
# return 0 = Il y a une case de vide
# return 1 = Le joueur a gagné
# return 2 = Match nul

def test_gagne(grille):
    # On teste si le joueur a gagné sur une ligne.
    if (grille[0][0]==grille[0][1]) and (grille[0][0]==grille[0][2]) and (grille[0][0]!=0):
        return 1
    if (grille[1][0]==grille[1][1]) and (grille[1][0]==grille[1][2]) and (grille[1][0]!=0):
        return 1
    if (grille[2][0]==grille[2][1]) and (grille[2][0]==grille[2][2]) and (grille[2][0]!=0):
        return 1

    # On teste si le joueur a gagné sur une colonne.
    if (grille[0][0]==grille[1][0]) and (grille[0][0]==grille[2][0]) and (grille[0][0]!=0):
        return 1
    if (grille[0][1]==grille[1][1]) and (grille[0][1]==grille[2][1]) and (grille[0][1]!=0):
        return 1
    if (grille[0][2]==grille[1][2]) and (grille[2][0]==grille[2][2]) and (grille[0][2]!=0):
        return 1

    # On teste si le joueur a gagné sur une diagonale.
    if (grille[0][0]==grille[1][1]) and (grille[0][0]==grille[2][2]) and (grille[0][0]!=0):
        return 1
    if (grille[0][2]==grille[1][1]) and (grille[0][2]==grille[2][0]) and (grille[0][2]!=0):
        return 1

    # On teste si il y a une case libre.
    for i in range(3):
        for j in range(3):
            if grille[i][j]==0:
                return 0
    return 2 #Match nul

# Début du jeu
def jouer(joueur, grille):
    Libellejoueur = str(joueur)
    ligne=input("C'est à vous joueur "+ Libellejoueur+" Entrez le numéro de la ligne : ")

# Boucle qui vérifie si le nombre est correctement saisi pour la ligne
    while (int(ligne) > 3 or int(ligne) < 1):
        ligne=input("Entrez un autre chiffre joueur "+Libellejoueur)

# Boucle qui vérifie si le nombre est correctement saisi pour la colonne
    colonne=input("Entrez le numéro de la colonne joueur "+Libellejoueur+": ")
    while (int(colonne) > 3 or int(colonne) < 1):
        colonne=input("Entrez un autre chiffre joueur "+ Libellejoueur)

# Tant que le joueur 1 joue sur une case déja prise, alors il rejoue
    while(grille[int(ligne)-1][int(colonne)-1] == 1 or grille[int(ligne)-1][int(colonne)-1] == 2):
        print("Cette case n'est pas disponible")
        ligne=input("Entrez le numéro de la ligne joueur "+ Libellejoueur +": ")
        colonne=input("Entrez le numéro de la colonne joueur "+ Libellejoueur+": ")
    if(joueur == 1):
        grille[int(ligne)-1][int(colonne)-1] = 1
    elif(joueur == 2):
        grille[int(ligne)-1][int(colonne)-1] = 2

etat_jeu = 0 # Permet de savoir si le jeu est terminé ou pas

grille = [[0,0,0],[0,0,0],[0,0,0]]
afficher_grille(grille)

# Boucle de jeu
while(etat_jeu == 0):
    # Joueur 1 joue
    jouer(1, grille)
    afficher_grille(grille)
    # On vérifie si joueur 1 a gagné ou match nul
    etat_jeu = test_gagne(grille)
    if (etat_jeu == 1):
        print("Joueur 1 a gagné !")
    elif (etat_jeu ==2):
        print("Match nul")
    # Joueur 2 joue
    if(etat_jeu == 0):
        jouer(2, grille)
        afficher_grille(grille)
    # On vérifie si joueur 2 a gagné ou match nul
        etat_jeu = test_gagne(grille)
        if (etat_jeu == 1):
            print("Joueur 2 a gagné !")
        elif (etat_jeu ==2):
            print("Match nul")
# Fin du jeu