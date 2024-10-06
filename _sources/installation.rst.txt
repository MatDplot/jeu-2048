Installer le package
====================

Pour installer le packages utiliser la commande::

	[jeu-2048/]$ python3 -m pip install -e .
	
ou::

	[jeu-2048/]$ python3 setup.py 
	
Sinon directement en clonnant le dépôt gitlab::

	$ git clone https://gitlab.in2p3.fr/mathis.dubau/jeu-2048
	$ cd jeu-2048
	[jeu-2048/]$ pip install .
	
Assurez vous d'avoir les droits administrateur pour installer le package sinon il faudra ajouter le package au path pour son bon fonctionnelent.



Utiliser le package
===================

Utiliser la commande::

	$ python3 -m jeu2048
	
ou directement::

	$ jeu2048

