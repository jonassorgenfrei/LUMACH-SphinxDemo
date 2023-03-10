# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here.
import os
import pathlib
import sys
sys.path.insert(0, pathlib.Path(__file__).parents[2].resolve().as_posix())

# add extensions
sys.path.append(os.path.abspath("./_ext"))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Lumache'
copyright = '2022, Jonas Sorgenfrei'
author = 'Jonas Sorgenfrei'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
# Napoleon for google type doc strings
extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'm2r2',
    # custom extension
    'helloworld',
    'todo',
    'recipe',
    'autodoc_intenum'
]

templates_path = ['_templates']
exclude_patterns = []

# Add the custom indices to the list of indices
html_use_index = True
html_domain_indices = True

# Set the index to be the RecipeIndex
#primary_domain = "recipe"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'furo'
#html_theme = 'alabaster'
html_static_path = ['_static']


# -- EPUB options -------------------------------------------------
epub_show_urls = 'footnote'

# -- TODO options -------------------------------------------------
todo_include_todos = True