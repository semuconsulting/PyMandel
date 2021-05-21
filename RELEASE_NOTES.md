# PyMandel Release Notes

### RELEASE 1.0.5

FIXES:

1. Fixed bug in `mandelpycli` command line utility that was skewing the zyoffset coordinate. Also minor improvements to metadata import. 

**NB:** If you have old (pre 0v1.0.0) metadata json files, they'll need amending to change the 
header element from `mandelpy` to `pymandel` - see examples in `images` folder.

### RELEASE 1.0.4

ENHANCEMENTS:

1. Further console script entry points added for pymandelcli and make_colormap CLI utilities. These utilities
can now be launched via simple `pymandelcli` and `make_colormap` commands.

### RELEASE 1.0.3

ENHANCEMENTS:

1. Console script entry point added to `setup.py`, so application can now be launched via a simple `pymandel` command as an alternative to `python -m pymandel`, provided the Python 3 scripts/bin folder is in the user's PATH.

### RELEASE 1.0.2

ENHANCEMENTS:

1. Numba now supports Python 3.9. Minimum numba version updated to 0.53.0.
2. Numba & numpy versions cited in About dialog.
