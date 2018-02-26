# Comsol compatible CET color set maker

Creates COMSOL compatible color encodings for the [CET perceptually uniform
colour maps](http://peterkovesi.com/projects/colourmaps/)

This is a quick one-off script, use as you will.
Joseph E. Weaver, jeweave4@ncsu.edu 


## Getting Started

`python make_comsol_compatible_cet_set.py`

### Prerequisites

Python 3 and either internet access or the CSV zip file from CET.
These tables work in COMSOL 4.3a, they probably work in other versions.

## Installation
If all goes well, a zip file containing tab separated values will be generated.
Just copy the text files from the zip to COMSOL's colortables directory.
For example, in COMSOL 4.3a:
`COMSOL/COMSOL43a/data/colortables`

You may have to restart COMSOL for this to take effect.

## Contact
For this script:
[Joe Weaver](jeweave4@ncsu.edu)

For the colormaps themselve and other data formats
[Peter Kovesi](peter.kovesi@uwa.edu.au)

## License

This project is licensed under the [GPL v3 license](gpl.md). 


## Acknowledgments
Peter Kovesi did all the hard work. I just wrote an overwrought regexp script.

Cite him!

Peter Kovesi. Good Colour Maps: How to Design Them.
arXiv:1509.03700 [cs.GR] 2015