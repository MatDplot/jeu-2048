Tests
=====

Vous pouvez tester le packages en utilisant la commande suivante::

	[jeu-2048/]$ pytest
	
Ceux-ci sont les suivants:

.. toctree::
   fct_tests

   
Pour accéder au résultats du tests utilisez les commandes suivantes::

	$ coverage run -m pytest
	$ coverage report
	$ coverage html
	

Les résultats du coverage présentent un taux de couverture de 90%. Cela vient du fait que nous utilisons une boucle pour jouer à une partie qui ne s'arrête qu'une fois la partie terminée. Il est donc difficile de test une telle boucle.
