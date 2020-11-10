# PyMandel

PyMandel is a graphical Mandelbrot and Julia Set (*and variants*) rendering application written entirely in Python 3.8 and tkinter 8.6, with metadata import/export, basic animation functionality and performance enhancement via Numba JIT compilation, parallelisation and caching.

![MacOS screenshot](/images/MacOS_Screenshot.png)

The application plots fractals in an expandable window and allows the user to save the image as a .png file. It automatically saves the metadata (settings) associated with an image and provides a facility to import that metadata at a later date to reproduce it.

It also includes both GUI and command line facilities to automatically create sequences of 'deep zoom' or 'spinning Julia Set' images which can be converted into animated GIF files or short videos (e.g. using external tools like GIMP or OpenShot).

### Current Status

![Release](https://img.shields.io/github/v/release/semuconsulting/PyMandel?include_prereleases)
![Build](https://img.shields.io/travis/semuconsulting/PyMandel)
![Release Date](https://img.shields.io/github/release-date-pre/semuconsulting/PyMandel)
![Last Commit](https://img.shields.io/github/last-commit/semuconsulting/PyMandel)
![Contributors](https://img.shields.io/github/contributors/semuconsulting/PyMandel.svg)
![Open Issues](https://img.shields.io/github/issues-raw/semuconsulting/PyMandel)

Beta. Application is fully functional.

Constructive feedback welcome.

#### Animated Mandelbrot Zoom sequence

This 178 frame, 10 fps sequence was automatically generated using the `mandelcli.py` command line utility and converted into an animated GIF file using GIMP. The entire sequence took about 50 seconds to render and save.

`python3 mandelcli.py filename="zoom" width=400 height=300 frames=178 zoom=0.75 zoominc=1.2 zxoffset=-0.743643887037158704752191506114774 zyoffset=0.131825904205311970493132056385139 theme="Colorcet_CET_C1"`

![Zoom Animation](/images/zoom.gif)

#### Animated Julia Spin sequences

These 400 frame, 20 fps sequences were automatically generated using the GUI's SPIN function and converted into animated GIF files using GIMP. The second sequence illustrates a Julia Set with exponent = 3.


![Spin Animation](/images/juliaspin.gif) ![Spin Animation Exponent = 3](/images/juliaspin_exp3.gif)

#### Sample Metadata

```
{"PyMandel": {
    "filename": "C:/Users/myuser/Downloads/mandela.png", 
    "created": "Apr 08 2020 19:43:41 GMT Standard Time", 
    "settype: "Mandelbrot",
    "zoom": 7500000000.0,
    "zoominc": 1.2,
    "frames": 10,
    "escradius": 2,
    "exponent": 2,
    "maxiter": 20000, 
    "zxoffset": -0.7491649396736062, 
    "zyoffset": 0.071803172645556,
    "cxoffset": 0, 
    "cyoffset": 0, 
    "theme": "Colorcet_CET_C1",
    "shift": 0
    }
}
```

## <a name="installation">Installation</a>

![Python version](https://img.shields.io/pypi/pyversions/PyMandel.svg?style=flat)

**NB**: At time of writing, there appears to be an issue installing `numba` on Python3.9 (specifically with `llvmlite`), so for
the time being users are recommended to use Python3.8.

In the following, `python` & `pip` refer to the python3 executables. You may need to type 
`python3` or `pip3`, depending on your particular environment.

### Dependencies

See [requirements.txt](requirements.txt).

On Windows and MacOS, pip, tkinter and the necessary imaging libraries are generally packaged with Python.  On some Linux distributions like Ubuntu 18+ and Raspberry Pi OS, they may need to be installed separately, e.g.:

`sudo apt-get install python3-pip python3-tk python3-pil python3-pil.imagetk`

The following python libraries are required (these will be installed automatically if using pip to install PyMandel):

`python -m pip install numba numpy Pillow`


### 1. Install using pip

[![PyPI version](https://img.shields.io/pypi/v/PyMandel.svg?style=flat)](https://pypi.org/project/PyMandel/)
![PyPI downloads](https://img.shields.io/pypi/dm/PyMandel.svg?style=flat)

The easiest way to install the latest version of PyMandel is via [pip](http://pypi.python.org/pypi/pip/):

`python -m pip install --upgrade PyMandel`

To run the application, if the python3 site_packages are in your PATH, simply type `python -m pymandel` (lowercase).

If not, type `python -m \full_path_to_site_packages\pymandel`.

**Tip**: to find the site_packages location, type `pip show PyMandel` and look for the `Location:` entry in the response, e.g.

- Linux: `Location: /home/username/.local/lib/python3.8/site-packages`
- MacOS: `Location: /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages`
- Windows: `Location: c:\users\username\appdata\local\programs\python\python38\lib\site-packages`

### 2. Manual installation

To install manually, download and unzip this repository and run:

`python -m /path_to_folder/foldername/pymandel` (lowercase)

e.g. if you downloaded and unzipped to a folder named `PyMandel-0.9.5`, run: 

`python -m /path_to_folder/PyMandel-0.9.5/pymandel`.

### Performance Optimisations

The application makes use of [Numba](http://numba.pydata.org/) just in time (jit) compilation, caching and parallelisation techniques, in conjunction with Numpy image arrays, to dramatically improve calculation and rendering times. 

**NB:** The very first time the program is used after installation, jit compilation and caching will delay the first plot by a couple of seconds, but thereafter the rendering should start instantly.

**NB:** While the Numba function decorators do afford a dramatic performance improvement over standard Python, we're not in the Ultra Fractal &copy; league here. But, hey, it's free and open source so have fun!

## How To Use

* Settings can be entered manually (or imported from a previously saved metadata file) to plot a fractal image using the specified parameters.

* Use the mouse wheel to zoom in and out at the current cursor location. There may be some lag at very high resolutions or where a substantial part of the image is within the set (i.e. black).

* Left-click, drag and release to zoom into a drawn rectangular area.

* Left-click momentarily to zoom in at the current cursor location by the Zoom Increment amount (e.g. a Zoom Increment of 10 will zoom in tenfold)

* Shift & Left-click to zoom out by the same amount.

* Right-clicking anywhere in the plot area will centre the image at that point using the currently specified zoom level.

* **NB:** Pressing Alt-L (left-hand Alt key) or Ctrl-L (left-hand Ctrl key) while left-clicking in Mandelbrot mode will automatically switch to Julia mode and plot the Julia Set corresponding to the cx, cy offset at the cursor location. Useful points of interest can be found anywhere around the perimeter of the Mandelbrot set.

* Pressing the Left &#9664; or Right &#9654; arrow keys in Julia mode will rotate the Julia Set clockwise or anti-clockwise about its origin (*the SPIN animation function does this automatically*).

* PLOT button - plot the image using current settings. 

* Cancel button - cancel the current plot operation.

* Reset button - reset the parameters to the default values.

* Save button - save the currently displayed image as a PNG file. You will be prompted for a directory on first use. A corresponding metadata json file will also be saved containing the parameters that were used to create the image, allowing it to be reproduced at a later date.

* File..Import Settings - import previously saved metadata. You will be prompted to select a json file to import.

* Zoom button - automatically create and save a sequence of images at increasing zoom levels, which can be converted externally into an animation (e.g. GIF or short video).

* Spin button - in Julia mode only, automatically creates and saves a 'spinning Julia Set' sequence. Increasing the number of frames will result in a slower but more detailed spin animation.

* Options..Hide/Show Status - toggles the Status Bar on or off.

* Options..Hide/Show Settings - toggles the Settings panel on or off.

* Help..How To - display how to use instructions.

* Help..About - display help screen with links to license and source code.

*Settings:*

* Set Type. Select from Mandelbrot, Julia, Tricorn or BurningShip. 

* Zoom level. The application currently uses standard 64-bit double precision and the maximum practical zoom level before floating-point errors cause pixelation is around 2 x 10<sup>13</sup> (20 million million).

* ZX axis offset in Real or 'Re' dimensional units (typically in the range -2.0 to 1.2).

* ZY axis offset in Imaginary or 'Im' dimensional units (typically in the range -1.2 to 1.2).

* CX axis offset of the Julia Set in Real or 'Re' dimensional units.

* CY axis offset of the Julia Set in Imaginary or 'Im' dimensional units.

* Max Iterations. Maximum number of iterations, which broadly equates to the fineness or resolution of the image. It will also affect the colour rendition in most themes. Higher zoom levels will typically require a higher number of iterations to produce a detailed image.

* Auto. If checked, maximum iterations will be automatically calculated according to the current zoom level.

* Escape Radius. The escape radius (normally 2.0).

* Exponent. The iteration exponent (normally 2 for the classic Mandelbrot, but higher exponents yield other radially symmetric forms at the cost of increased rendering time).

* Theme - a list of color rendering themes is provided. These are based on a variety of rendering algorithms, including cyclic colormap indexing; HSV derivations; banded RGB maps and simple grayscale. The code allows additional algorithms to be easily added.

* Theme Shift - this modifies the characteristics of certain themes, typically by shifting the hue along the spectrum or color map index. Its effect will depend on the specific rendering algorithm used.

* An image filename for saved images, metadata and animation frames.

* Frames. The number of animation frames to create.

* Zoom Increment. The zoom increment between frames (e.g. an increment of 1.5 means each successive frame is zoomed in 1.5x as much as the previous one; set Zoom Increment < 1 to zoom out). Used for left-click zooms and animations. For animations, the number of iterations is also automatically increased with the zoom level in accordance with a predefined algorithm.

## Command Line Utilities

### mandelcli.py

`mandelcli.py` is a command line equivalent to the GUI's Animate function. It can be invoked using keyword parameters 
e.g. `python mandelcli.py width=480 height=480 frames=20` to produce a sequence of .png images. Pass `-h` or `-help` for a list of available parameters.

It can import settings from a previously saved metadata file using the import parameter e.g. `import=filename.json`.

In addition to producing animated sequences, the command line utility can be used to create single images at a much higher pixel resolution than would be available via the GUI application on a standard monitor, though render time may be significant.

** Suggestion ** Use the PyMandel GUI at moderate resolutions to explore fractals and find a location and configuration you like, save the image & metadata, and then use the `mandelcli.py` command line utility to import the metadata and create a much higher resolution version of the same image e.g for desktop wallpaper, printing or sharing.

### make_colormap.py

`make_colormap.py` is a simple command line utility for generating PyMandel-compatible numpy RGB arrays from image files containing suitable color gradients (e.g. created using GIMP's gradient tool) or even photographs with interesting color palettes. It takes the following optional keyword parameters:

`python gen_colormap.py mapname=mymap input=image.png output=mymap_colormap.py levels=256`

## License

![License](https://img.shields.io/github/license/semuconsulting/PyMandel.svg)

BSD 3-Clause License

Copyright (c) 2020, SEMU Consulting
All rights reserved.

The HoloViz [Colorcet color maps](https://github.com/holoviz/colorcet) library has been harvested for some of the color rendering themes. These color maps are released under a Creative Commons Attribution 4.0 International Public License (CC-BY) - see [Colorcet License Conditions](https://github.com/holoviz/colorcet/blob/master/LICENSE.txt) for details. ***NB:*** for convenience the selected Colorcet assets (256-depth cyclic color maps) were converted into numpy rgb arrays in colormaps.py and the library itself is not actually used at runtime.

## Author Information

semuadmin@semuconsulting.com
