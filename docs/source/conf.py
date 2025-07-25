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
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Cumulator and collectors to calculatie values in various ways'
copyright = '2025-2025, Günter Pöhl'
author = 'Günter Pöhl'

version ='0.1.0'
# The full version, including alpha/beta/rc tags
release = '0.1.0 alpha'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
	'sphinx.ext.todo',
 	'sphinx_rtd_theme',
	'sphinxcontrib.phpdomain',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []



# load PhpLexer
from sphinx.highlighting import lexers
from pygments.lexers.web import PhpLexer

# enable highlighting for PHP code not between <?php ... ?> by default
lexers['php'] = PhpLexer(startinline=True, lineos=1)
lexers['php-annotations'] = PhpLexer(startinline=True, lineos=1)
primary_domain = 'php'


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"
              

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']

html_context = {
	# Enable the "Edit in GitHub link within the header of each page.
	"display_github": True,
	"github_user": "gpoehl",
	"github_repo": project,
	"github_version": "master/",
	"conf_py_path": "/docs/", 
#	"source_suffix": source_suffix,
}	
project_name = '**cumulator**'
rst_epilog = '.. |project_name| replace:: %s' % project_name
todo_include_todos = True
