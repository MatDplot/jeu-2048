Règles
======

Les règles du jeu 2048 sont simples: vous devez former le nombre 2048. Pour cela vous devez bouger les nombres sur le plateau pour les combiner. Les mouvements possibles sont les suivants:

.. math::

	\begin{bmatrix} 8 & 4 & 0 & 0 \end{bmatrix} \xleftarrow{q} \begin{bmatrix} 8 & 2 & 2 & 0 \end{bmatrix} \xrightarrow{d} \begin{bmatrix} 0 & 0 & 8 & 4 \end{bmatrix}
	
	
.. math::

	\begin{bmatrix} 8 \\ 4 \\ 0 \\ 0 \end{bmatrix} \xleftarrow{z} \begin{bmatrix} 8 \\ 2 \\ 2 \\ 0 \end{bmatrix} \xrightarrow{s} \begin{bmatrix} 0 \\ 0 \\ 8 \\ 4 \end{bmatrix}
	
	
Ainsi on se déplace avec les commandes z, q, s et d pour faire 'glisser' les nombres dans la direction choisie. Il vont s'additionner entre eux s'ils sont égaux.

Après avoir déplacé le plateau, un 2 (80%) ou un 4 (20%) va apparaitre de manière aléatoire. 

Si vous ne pouvez plus faire de mouvement vous avez perdu.

Dans cette version vous pouvez choisir la taille du plateau (carré). Plus celui-ci est grand plus c'est facile.
