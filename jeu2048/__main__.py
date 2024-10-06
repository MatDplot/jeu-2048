"""
Lancement du package et du jeu
"""
from .game import D2048

def main():
    """
    Fonction principale du package
    """
    print("Jeu 2048 \n")
    print("commandes: \n haut = z")
    print(" bas = s \n gauche = q \n droite= d")
    taille = input("Taille du plateau:")
    print(D2048(int(taille)))

if __name__ == '__main__':
    main()
