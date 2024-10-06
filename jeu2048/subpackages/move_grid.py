"""
Module permettant d'effectuer les mouvements du plateau
"""

def move_ligne(ligne):
    """
    Déplacement d'un liste selon les règles du 2048

    :param list ligne: Ligne du plateau
    :return: Ligne déplacée vers la gauche en sommant suivant les règles
    :rtype: list
    """
    lignep = []
    lignepp = []
    for i in ligne:
        if i != 0:
            lignep.append(i)
    dejavu = False
    for indx, i in enumerate(lignep):
        if dejavu is True:
            dejavu = False
            continue
        if dejavu is False:
            if indx < len(lignep)-1:
                if lignep[indx] == lignep[indx+1]:
                    lignepp.append(lignep[indx]*2)
                    dejavu = True
                else:
                    lignepp.append(lignep[indx])
            else:
                lignepp.append(lignep[indx])
    while len(lignepp) < len(ligne):
        lignepp.append(0)
    return lignepp

def colonne(matrix, i):
    """
    Conversion d'un colonne en une liste

    :param list matrix: Matrice 2D
    :param int i: Indice de la colonne
    :return: Liste des élèments de la ième colonne
    :rtype: list
    """
    return [ligne[i] for ligne in matrix]


def move_grid(grid, mvmt):
    """
    Déplacement du plateau dans la direction choisie

    :param list grid: Matrice 2D
    :param str mvmt: Mouvement à effecteur
    :return: Plateau déplacé selon la direction choisie
    :rtype: list[list[int]]
    """
    gridp = []
    if mvmt == 'd':
        for i in grid:
            gridp.append(list(reversed(move_ligne(list(reversed(i))))))
    if mvmt == 'q':
        for i in grid:
            gridp.append(move_ligne(i))
    if mvmt == 'z':
        matrice = []
        for i in range(len(grid[0])):
            matrice.append(move_ligne(colonne(grid,i)))
        for i in range(len(grid[0])):
            gridp.append(colonne(matrice,i))
    if mvmt == 's':
        matrice = []
        for i in range(len(grid[0])):
            matrice.append(list(reversed(move_ligne(list(reversed(colonne(grid,i)))))))
        for i in range(len(grid[0])):
            gridp.append(colonne(matrice,i))
    return gridp
