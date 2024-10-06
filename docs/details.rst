Packaging (`setup.cfg`)
-----------------------

Le fichier :ref:`setup.cfg` permet d'installer et paramétrer facilement le package::

  $ pip install pyyc

ou lors du clonage du `dépôt GitLab <https://gitlab.in2p3.fr/mathis.dubau/jeu-2048>`_::

  $ git clone https://gitlab.in2p3.fr/mathis.dubau/jeu-2048  
  $ cd pyyc
  $ pip install .                                  
  
Package initialization (`__init__.py`)
--------------------------------------

Le fichier `__init__.py` dans chaque dossier du package initialise les import de chaque module.


Main entries (`__main__.py`)
----------------------------

Le progamme *main* peut être appelé de différentes façon:

* comme le :ref:`__main__.py <main.py>` entry d'un module module

  Il ne peut y avoir qu'un package main, correspondant au `if
  __name == "__main__"` du fichier `__main__.py`.

* en tant que scripts défini comme point d'éntré dans :ref:`setup.cfg`:

  .. literalinclude:: ../setup.cfg
     :language: cfg
     :start-at: [options.entry_points]
     :end-before: [options.extras_require]

  Ces points d'entrés sont convertit en scripts::

    $ jeu2048      # exécute jeu2048/__main__.py:main()
