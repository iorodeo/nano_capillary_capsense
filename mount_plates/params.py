""" 
Parameters dictionaries. 
"""

INCH2MM = 25.4

capillary = {
        'length'   : 127.0,
        'diameter' : 1.05, 
        'color'    : (0.1,0.4,1.0,0.6),
        }

base_pcb = {
        'size'                 : (9*INCH2MM, 3.25*INCH2MM, 0.062*INCH2MM),
        'color'                : (0.1,0.9,0.1,1.0), 
        'mount_hole_diam'      : 0.116*INCH2MM,  
        'mount_hole_offset'    : 0.12*INCH2MM,
        'capillary_number'     : 4,
        'capillary_spacing'    : 1.4*INCH2MM,
        'capillary_pad_right'  : 0.25*INCH2MM,
        'capillary_tolerance'  : 0.15,
        'sandwich_hole_num'    : 1, 
        'sandwich_hole_diam'   : 0.116*INCH2MM,
        'sandwich_hole_offset' : 0.5*3.25*INCH2MM, 
        }

spacer_pcb = {
        'size'  : (0.4*INCH2MM, 3.25*INCH2MM, 0.031*INCH2MM),
        'color' : (0.8,0.4,0.4,1.0),
        }

top_pcb = {
        'size' : (2*spacer_pcb['size'][0]+capillary['diameter']+base_pcb['capillary_tolerance'],3.25*INCH2MM, 0.062*INCH2MM),
        'color': (1.0, 1.0, 0.0, 1.0),
        }

back_plate = {
        'thickness'     : 4.5, 
        'color'         : (0.6, 0.2, 0.7, 1.0), 
        'hole_diameter' : 0.085*INCH2MM
        }

standoff = {
        'color'         : (0.65, 0.65, 0.65), 
        'diameter'      : 0.25*INCH2MM,
        'height'        : 0.5*INCH2MM,
        'hole_diameter' : 0.116*INCH2MM,
        }

fourforty = {
        'color'          : (0.6, 0.6, 0.6, 1.0), 
        'shaft_diameter' : 0.1*INCH2MM,
        'shaft_length'   : 0.25*INCH2MM,
        'head_diameter'  : 0.211*INCH2MM,
        'head_thickness' : 0.05*INCH2MM,
        }

thumbscrew = {
        'color'          : (0.6, 0.6, 0.6, 1.0), 
        'shaft_diameter' : 0.1*INCH2MM,
        'shaft_length'   : 0.3125*INCH2MM,
        'head_diameter'  : 0.375*INCH2MM,
        'head_thickness' : 0.3125*INCH2MM,
        }

top_magnet = {
        'color'          : (0,0,0,1),
        'diameter'       : (1.0/8.0)*INCH2MM,
        'height'         : (1.0/32.0)*INCH2MM,
        }

bottom_magnet = {
        'color'          : (0,0,0,1),
        'diameter'       : (1.0/8.0)*INCH2MM,
        'height'         : (1.0/16.0)*INCH2MM,
        }


multi_assembly = {
        'num'     : 5,
        'spacing' : 0.5*INCH2MM,
        }

assembly_mount_plate = {
        'margin_x'             : 1.5*INCH2MM, 
        'margin_y'             : 0.25*INCH2MM,
        'thickness'            : 6.0, 
        'fourforty_tap_diam'   : 0.085*INCH2MM,
        'qtr_twenty_thru_diam' : 0.257*INCH2MM,
        'qtr_twenty_offset'    : 0.5*INCH2MM,
        }
