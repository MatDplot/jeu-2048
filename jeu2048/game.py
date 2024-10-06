"""
Création de la classe D2048 qui générèe une partie du jeu 2048
"""

from .subpackages import grid_setup
from .subpackages import move_grid

class D2048:
    """
    Classe générant le jeu 2048 sur une grille de taille donnée
    """
    def __init__(self, taille):
        self.taille = taille
        self.grid = grid_setup.init_grid(self.taille)
        self.mvmt = ""
        for _ in range(self.taille-1):
            self.grid = grid_setup.random_grid(self.grid)

    def __str__(self):
        return self.jouer()

    def demande_mvmt(self,  texte):
        """
        Demande du mouvement à effectuer par le joueur selon les possibilités

        :param list texte: Liste contenant les coups possibles
        :return: Mouvement choisie par le joueur
        :rtype: str
        """
        display_texte = ""
        for i in texte:
            display_texte += i + " "
        display_texte += ":"

        input_user = False
        while input_user is False:
            mvmt = input(display_texte)
            if mvmt in texte:
                input_user = True
            else:
                mvmt = print("Entrez une commande valide")
        return mvmt

    def prevision(self, grid):
        """
        Prévision des coups possibles que le joueur peut effectuer

        :param list grid: Matrice 2D
        :return: Mouvements possibles sinon 'perdu'
        :rtype: list ou str
        """
        mvmt = ['q','d','s','z']
        if move_grid.move_grid(grid,'q') == grid:
            mvmt.remove('q')
        if move_grid.move_grid(grid,'d') == grid:
            mvmt.remove('d')
        if move_grid.move_grid(grid,'s') == grid:
            mvmt.remove('s')
        if move_grid.move_grid(grid,'z') == grid:
            mvmt.remove('z')
        if not mvmt:
            return 'perdu'
        return mvmt

    def endgame(self, grid):
        """
        Vérification de la condition de victoire

        :param list grid: Matrice 2D
        :return: Victoire sinon string vide
        :rtype: str
        """
        for i in grid:
            if 2048 in i:
                return 'victoire'
        return ''

    def jouer(self):
        """
        Déroulement d'une partie
        """
        perdu = False
        victoire = False
        while perdu is False and victoire is False:
            grid_setup.show_grid(self.grid)
            mvmt_possible = self.prevision(self.grid)
            if mvmt_possible =='perdu':
                perdu = True
                continue
            self.mvmt = self.demande_mvmt(mvmt_possible)
            self.grid = move_grid.move_grid(self.grid, self.mvmt)
            if self.endgame(self.grid) == 'victoire':
                victoire = True
                grid_setup.show_grid(self.grid)
                continue
            self.grid = grid_setup.random_grid(self.grid)
        if perdu is True:
            color = f"{grid_setup.Couleurs.red}{grid_setup.Couleurs.bold}"
            return color + f"PERDU! {grid_setup.Couleurs.white} \n Partie terminée"
        if victoire is True:
            color = f"{grid_setup.Couleurs.blue}{grid_setup.Couleurs.bold}"
            return color + f"GAGNE! {grid_setup.Couleurs.white} \n Partie terminée"
