# gerber merging as gerbv-projects
Construct a panelized gerbv project, which you can 
then export as panel gerbers. Tested with gerbv 
version 2.6A.

The tool is meant for cases where you can only have 
access to gerber files and you don't want to pay for 
expensive tools (which don't do much more than this 
script, at least for my own purposes).

The open source gerber viewer, gerbv 
(http://gerbv.sourceforge.net/) has utilities for 
viewing and merging gerber files. It lacks convenient
UI for doing panels inside the program though.

Since the panelizing features are not there yet, 
here's the simplest Python script to create a gerbv 
project file (.gvp), which you can open with gerbv 
and manually export the layers to a combined panel 
gerber file.

# Usage
The script uses python 3.5.*, has no fancy input 
parsing (yet) and takes five command line parameters:

1. folder, in which all gerber files for the layers 
of a single board are located in.
2. number of rows in the panel
3. number of columns in the panel
4. x offset in mm
5. y offset in mm

Thus, an example call would be:
./merge_into_gerbv_project.py myproject/ 3 2 100 80

which would produce a layout where bottom left is the 
origin, and 2nd column is shifted 100 mm right, 
2nd row is shifted 80 mm up and 3rd row is shifted 
160 mm up.

You need to draw your panel design (fiducials, possible 
frame to fit the palette, board break tabs etc.) with 
your favourite pcb tool, such as KiCad. Then 
export the panel frame and other stuff as gerbers 
and use the gerbv to combine it with your merged 
gerbers.
