#!/usr/bin/python

# takes: 1. <folder of gerbers>
#        2. <panel-rows>
#        3. <panel-columns>
#        4. <panel-x-offset>
#        5. <panel-y-offset>
#        6. <pos-low-left-x>
#        7. <pos-low-left-y>
#        8. <board-pos-x>
#        9. <board-pos-y>

import sys
import random

from pathlib import Path

base_dir = Path(sys.argv[1])

panel_rows = int(sys.argv[2])
panel_cols = int(sys.argv[3])

panel_offset_x = float(sys.argv[4])
panel_offset_y = float(sys.argv[5])

pos_low_left_x = float(sys.argv[6])
pos_low_left_y = float(sys.argv[7])

board_pos_x = float(sys.argv[8])
board_pos_y = float(sys.argv[9])

all_offset_x = -board_pos_x+pos_low_left_x
all_offset_y = -board_pos_y+pos_low_left_y

MM_to_INCH = 0.0393700787; #from google

def random_color_setting():
    return "\t(cons 'color #(" \
        + str(random.randint(2**12,2**16)) \
        + " " + str(random.randint(2**12,2**16)) \
        + " " + str(random.randint(2**12,2**16)) \
        + "))\n"

def visibility_setting(visible):
    return "\t(cons 'visible #" + ("t" if visible else "f")\
        + ")\n"

def translation_setting(row,col):
    x = row*panel_offset_x + all_offset_x
    y = col*panel_offset_y + all_offset_y
    return "\t(cons 'translate #(" \
        + str(x*MM_to_INCH) + " " + str(y*MM_to_INCH) \
        + "))\n"

def layer_definition(filename, row, col, ordnum):
    return "(define-layer! " + str(ordnum) \
        + " (cons 'filename \"" + filename + "\")\n" \
        + visibility_setting(False) \
        + random_color_setting() \
        + translation_setting(row, col) \
        + ")\n"
project_filename = str(base_dir.absolute()) \
                    + "/" + base_dir.parts[-1] \
                    + ".gvp"
project_file = open(project_filename, "w")
print(project_filename)
layers_of_all_boards = panel_cols*panel_rows*len(list(base_dir.iterdir()))

current_layer_num = layers_of_all_boards

project_file.write("(gerbv-file-version! \"2.0A\")\n")
for file in base_dir.iterdir():
    filename = file.parts[1]
    if not filename.endswith(".gvp"):
        for row in range(panel_rows):
            for col in range(panel_cols):
                project_file.write( 
                    layer_definition(
                        filename, row, col, current_layer_num))
                current_layer_num = current_layer_num-1
            
project_file.write("(define-layer! -1 (cons 'filename \"" \
                   + str(base_dir.absolute()) + "\")\n" \
                   + "\t(cons 'color #(0 0 0))\n" \
                   + ")\n" \
                   + "(set-render-type! 0)\n")

project_file.close()
