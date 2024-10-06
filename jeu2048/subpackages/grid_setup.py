"""
Module permettant de paramétrer et d'afficher la grille de jeu
"""
import random
import math

class Couleurs:
    """
    Définition des couleurs du terminal
    """
    purple = '\033[95m'
    blue = '\033[94m'
    cyan = '\033[96m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    white = '\033[0m'
    bold = '\033[1m'

def init_grid(taille):
    """
    Création d'un plateau vide

    :param int taille: Taille du plateau
    :return: Matrice 2D
    :rtype: list[list[int]]
    """
    return [[0 for i in range(taille)] for j in range(taille)]

def max_grid(grid):
    """
    Cherche le nombre de digits dans le plus grand nombre du plateau

    :param list grid: Matrice 2D
    :return: Nombre de digits du maximum de la matrice
    :rtype: int
    """
    max_n = 0
    for i in grid:
        if max(i) > max_n:
            max_n = max(i)
    if max_n > 0:
        digits = int(math.log10(max_n))+1
    elif max_n == 0:
        digits = 1
    return digits

def taille_str_nombre(space_number,i):
    """
    Modifie la taille (au sens taille du string) d'un nombre
    pour qu'elle convienne à une autre

    :param int space_number: Taile final du string
    :param str i: Nombre à rallonger
    :return: Le même nombre qui correspond à la taille donnée
    :rtype: str
    """
    iprime = i
    count = 0
    while len(iprime) < space_number:
        iprime += " "
        count +=1
    return count * " " +i

def color(i,space_number):
    """
    Définit les couleurs à afficher pour les différents nombres possibles
    Puissances de 2 jusqu'à 2048

    :param int i: Nombre
    :param int space_number: Taille du string
    :return: String avec les couleurs en fonction de la valeur de i et la taille aqéquates
    :rtype: str
    """
    nombre = taille_str_nombre(space_number,str(i))
    if i == 0:
        phrase = f"{Couleurs.white}" + nombre + f"{Couleurs.white}"
    if i == 2:
        phrase = f"{Couleurs.green}" + nombre + f"{Couleurs.white}"
    if i == 4:
        phrase = f"{Couleurs.cyan}" + nombre + f"{Couleurs.white}"
    if i == 8:
        phrase = f"{Couleurs.blue}" + nombre + f"{Couleurs.white}"
    if i == 16:
        phrase = f"{Couleurs.yellow}" + nombre + f"{Couleurs.white}"
    if i == 32:
        phrase = f"{Couleurs.red}" + nombre + f"{Couleurs.white}"
    if i == 64:
        phrase = f"{Couleurs.purple}" + nombre + f"{Couleurs.white}"
    if i == 128:
        phrase = f"{Couleurs.green}{Couleurs.bold}" + nombre + f"{Couleurs.white}"
    if i == 256:
        phrase = f"{Couleurs.blue}{Couleurs.bold}" + nombre + f"{Couleurs.white}"
    if i == 512:
        phrase = f"{Couleurs.yellow}{Couleurs.bold}" + nombre + f"{Couleurs.white}"
    if i == 1024:
        phrase = f"{Couleurs.red}{Couleurs.bold}" + nombre + f"{Couleurs.white}"
    if i == 2048:
        phrase = f"{Couleurs.purple}{Couleurs.bold}" + nombre + f"{Couleurs.white}"
    return phrase

def show_grid(grid):
    """
    Affichage du plateau dans le terminal

    :param list grid: Matrice 2D
    :return: Affiachge du plateau dans le terminal
    """
    space_number = max_grid(grid)
    paragraphe = "\n"
    for i in grid:
        phrase = " "
        for j in i:
            phrase += str(color(j,space_number)) + "  "
        paragraphe += phrase + "\n"
    print(paragraphe)


def random_grid(grid):
    """
    Placmement d'un 2 à 80% et d'un 4 à 20% de chance

    :param list grid: Matrice 2D
    :return: Plateau initial avec un 0 changé en 2 (80%) ou 4 (20%)
    :rtype: list[list[int]]
    """
    coord = []
    for indx_i, i in enumerate(grid):
        for indx_j, j in enumerate(i):
            if j == 0:
                coord.append([indx_i,indx_j])
    proba = random.uniform(0,1)
    if proba <= 0.8:
        chiffre = 2
    else:
        chiffre = 4
    coord_random = random.randint(0, len(coord)-1)
    grid[coord[coord_random][0]][coord[coord_random][1]] = chiffre
    return grid
