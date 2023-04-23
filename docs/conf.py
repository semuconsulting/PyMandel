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

# sys.path.clear()
# paths = [
#     "/Library/Frameworks/Python.framework/Versions/3.10/bin",
#     "/Library/Frameworks/Python.framework/Versions/3.10/lib/python310.zip",
#     "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10",
#     "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/lib-dynload",
#     "/Users/steve/Library/Python/3.10/lib/python/site-packages",
#     "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages",
#     "../src",
# ]
# for p in paths:
#     sys.path.insert(0, os.path.abspath(p))

sys.path.insert(0, os.path.abspath("../src"))
print(sys.path)

from pymandel import version as VERSION

# -- Project information -----------------------------------------------------

project = "PyMandel"
copyright = "2021, SEMU Consulting"
author = "SEMU Consulting"

# The full version, including alpha/beta/rc tags
release = VERSION
version = VERSION

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ["sphinx.ext.autodoc", "sphinx.ext.viewcode"]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"
html_title = "<project> v<version> documentation."

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ["_static"]
html_last_updated_fmt = "%b %d %Y"
html_theme_options = {
    "display_version": True,
}

autodoc_default_options = {
    "members": True,
    "member-order": "bysource",
    "special-members": "__init__",
    "undoc-members": True,
    "exclude-members": "__weakref__",
}
