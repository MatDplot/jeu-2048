"""
Fonction pour paramétrer la grille de jeu ainsi
que de permettre le deplacement des nombres de la grille
"""

__all__ = ['grid_setup', 'move_grid']

for _mod in __all__:
    __import__(__name__ + '.' + _mod, fromlist=[None])
