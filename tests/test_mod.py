"""
Test des fonctions du :mod:`subpackages`. A utiliser avec:

    $ pytest -v test_mod.py
"""

import pytest
import jeu2048

def test_init_grid():
    """
    Test initialisation du plateau
    """
    plateau_test = [[0 for i in range(4)] for j in range(4)]

    assert jeu2048.subpackages.grid_setup.init_grid(4) == plateau_test


def test_max_grid():
    """
    Test du nombre de digits du plus grand nombre du plateau
    """
    test1 = [[1,10],[100,1000]]
    test2 = [[0,0],[0,0]]

    assert jeu2048.subpackages.grid_setup.max_grid(test1) == 4
    assert jeu2048.subpackages.grid_setup.max_grid(test2) == 1


def test_taille_str_nombre():
    """
    Test du nombre d'espaces devant un nombre
    """

    assert jeu2048.subpackages.grid_setup.taille_str_nombre(3,str(2)) == "  2"
    assert jeu2048.subpackages.grid_setup.taille_str_nombre(2,str(10)) == "10"
    assert jeu2048.subpackages.grid_setup.taille_str_nombre(0,str(1)) == "1"


def test_show_grid(capsys):
    """
    Test de l'affichage du plateau
    """
    plateau_test = [[0,4],[2,0]]
    expect = "\n \x1b[0m0\x1b[0m  \x1b[96m4\x1b[0m  \n \x1b[92m2\x1b[0m  \x1b[0m0\x1b[0m  \n\n"

    jeu2048.subpackages.grid_setup.show_grid(plateau_test)
    captured = capsys.readouterr()
    assert captured.out == expect

def test_color(capsys):
    """
    Test de l'affichage des couleurs
    """

    color1 = jeu2048.subpackages.grid_setup.color(0,5)
    expect1 = "\033[0m    0\033[0m"
    assert color1 == expect1
    color1 = jeu2048.subpackages.grid_setup.color(2,5)
    expect1 = "\033[92m    2\033[0m"
    assert color1 == expect1
    color1 = jeu2048.subpackages.grid_setup.color(4,5)
    expect1 = "\033[96m    4\033[0m"
    assert color1 == expect1
    color1 = jeu2048.subpackages.grid_setup.color(8,5)
    expect1 = "\033[94m    8\033[0m"
    assert color1 == expect1
    color1 = jeu2048.subpackages.grid_setup.color(16,5)
    expect1 = "\033[93m   16\033[0m"
    assert color1 == expect1
    color1 = jeu2048.subpackages.grid_setup.color(32,5)
    expect1 = "\033[91m   32\033[0m"
    assert color1 == expect1
    color1 = jeu2048.subpackages.grid_setup.color(64,5)
    expect1 = "\033[95m   64\033[0m"
    assert color1 == expect1
    color1 = jeu2048.subpackages.grid_setup.color(128,5)
    expect1 = "\033[92m\033[1m  128\033[0m"
    assert color1 == expect1
    color1 = jeu2048.subpackages.grid_setup.color(256,5)
    expect1 = "\033[94m\033[1m  256\033[0m"
    assert color1 == expect1
    color1 = jeu2048.subpackages.grid_setup.color(512,5)
    expect1 = "\033[93m\033[1m  512\033[0m"
    assert color1 == expect1
    color1 = jeu2048.subpackages.grid_setup.color(1024,5)
    expect1 = "\033[91m\033[1m 1024\033[0m"
    assert color1 == expect1
    color1 = jeu2048.subpackages.grid_setup.color(2048,5)
    expect1 = "\033[95m\033[1m 2048\033[0m"
    assert color1 == expect1

def test_random_grid():
    """
    Test du changement aléatoire de zéro en 2 ou 4
    """
    plateau_test = [[0,2],[2,2]]
    plateau_prime = jeu2048.subpackages.grid_setup.random_grid(plateau_test)

    assert plateau_prime[0][0] != 0

def test_move_ligne():
    """
    Test du déplacement d'une ligne selon vers la droite en sommant selon les rèlges du 2048
    """

    ligne_test = [0,2,2,4,4,8]
    ligne_prime = jeu2048.subpackages.move_grid.move_ligne(ligne_test)
    expect = [4,8,8,0,0,0]

    assert ligne_prime == expect

def test_colonne():
    """
    Test de la conversion d'un colonne en une liste
    """

    plateau_test = [[1,2],[3,4]]
    plateau_prime1 = jeu2048.subpackages.move_grid.colonne(plateau_test,0)
    plateau_prime2 = jeu2048.subpackages.move_grid.colonne(plateau_test,1)

    assert plateau_prime1 == [1,3]
    assert plateau_prime2 == [2,4]

def test_move_grid():
    """
    Test du déplacement du plateau
    """

    plateau_test = [[2,2],[2,2]]

    plateau_prime_z = jeu2048.subpackages.move_grid.move_grid(plateau_test,'z')
    plateau_prime_q = jeu2048.subpackages.move_grid.move_grid(plateau_test,'q')
    plateau_prime_s = jeu2048.subpackages.move_grid.move_grid(plateau_test,'s')
    plateau_prime_d = jeu2048.subpackages.move_grid.move_grid(plateau_test,'d')

    assert plateau_prime_z == [[4,4],[0,0]]
    assert plateau_prime_q == [[4,0],[4,0]]
    assert plateau_prime_s == [[0,0],[4,4]]
    assert plateau_prime_d == [[0,4],[0,4]]


def test_demande_mvmt(monkeypatch):
    """
    Test de la demande de mouvement
    """
    expect1 = 'z'
    monkeypatch.setattr('builtins.input', lambda _: expect1)
    input1 = jeu2048.game.D2048.demande_mvmt(0,['z','q','s','d'])
    assert input1 == 'z'


def test_prevision():
    """
    Test de la prévision des mouvements
    """

    plateau_test = [[2,4],[8,16]]

    assert jeu2048.game.D2048.prevision(0,plateau_test) == 'perdu'

def test_victoire():
    """
    Test de la condition de victoire
    """

    plateau_test = [[0,2048],[2,4]]

    assert jeu2048.game.D2048.endgame(0,plateau_test) == 'victoire'

    plateau_test[0][1] = 0
    assert jeu2048.game.D2048.endgame(0,plateau_test) == ''
