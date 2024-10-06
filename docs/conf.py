# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('..'))

import jeu2048

# -- Project information -----------------------------------------------------

project = 'jeu2048'
copyright = '2022, Mathis Dubau'
author = 'Mathis Dubau'

# The full version, including alpha/beta/rc tags
from jeu2048 import __version__
release = __version__


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx', 
    'sphinx.ext.mathjax',  
    'sphinx.ext.viewcode',
    'sphinx.ext.extlinks',     
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
]

# Autodoc configuration
autodoc_default_options = {
    'members': True,            # Document all members
    'undoc-members': True,      # ... including undocumented ones
    'ignore-module-all': True,  # do not stick to __all__
}
autoclass_content = "both"              # Insert class and __init__ docstrings
autodoc_member_order = "bysource"       # Keep source order

# Intersphinx configuration
intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'pytest': ('https://docs.pytest.org/en/7.1.x/', None),
}

# Autosectionlabel configuration
autosectionlabel_prefix_document = True  # :ref:`fichier:section`

# Coverage configuration
coverage_show_missing_items = True

# mathjax configuration
mathjax3_config = {
    'tex': {'tags': 'ams', 'useLabelIds': True},
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store',
                    '**.egg-info']

# The reST default role (used for this markup: `text`) to use for all
# documents.
default_role = 'literal'

highlight_language = 'console'

# If true, '()' will be appended to :func: etc. cross-reference text.
add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
show_authors = True

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'emacs'

# If true, keep warnings as "system message" paragraphs in the built documents.
keep_warnings = True


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'bizstyle'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = True
