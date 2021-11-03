#!/usr/bin/env python
"""
Setup script for PyMandel Application

python setup.py sdist bdist_wheel

Created on 5 Apr 2020

@author: semuadmin
"""

from setuptools import setup, find_packages
from pymandel import version as VERSION

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="PyMandel",
    version=VERSION,
    packages=find_packages(),
    install_requires=["numba>=0.53.1", "numpy>=1.18.3", "Pillow>=7.1.2"],
    package_data={
        "pymandel": [
            "resources/*.gif",
            "resources/*.png",
            "resources/*.ico",
            "resources/*.icns",
            "images/*.png",
        ],
    },
    entry_points={
        "console_scripts": [
            "pymandel = pymandel.__main__:main",
            "pymandelcli = pymandel.mandelcli:main",
            "make_colormap = colormaps.make_colormap:main",
        ]
    },
    include_package_data=True,
    author="semuadmin",
    author_email="semuadmin@semuconsulting.com",
    description="PyMandel Fractal Generator Application",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/semuconsulting/PyMandel",
    license="BSD 3-Clause 'Modified' License",
    keywords="PyMandel fractal mandelbrot julia numba",
    platforms="Windows, MacOS, Linux",
    project_urls={
        "Bug Tracker": "https://github.com/semuconsulting/PyMandel",
        "Documentation": "https://github.com/semuconsulting/PyMandel",
        "Source Code": "https://github.com/semuconsulting/PyMandel",
    },
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Development Status :: 5 - Production/Stable",
        "Environment :: MacOS X",
        "Environment :: X11 Applications",
        "Environment :: Win32 (MS Windows)",
        "Intended Audience :: End Users/Desktop",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Desktop Environment",
        "Topic :: Education",
        "Topic :: Games/Entertainment",
    ],
)
