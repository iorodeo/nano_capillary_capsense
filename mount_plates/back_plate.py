import scipy
from py2scad import *
import params


class BackPlate(object):

    def __init__(self,params=params):
        self.params = params
        self.__make()

    def __str__(self):
        return self.part.__str__()

    def __make(self):
        # Create main plate
        cap_numb = self.params.base_pcb['capillary_number'] 
        cap_spac = self.params.base_pcb['capillary_spacing']
        cap_diam = self.params.capillary['diameter']
        spacer_x, spacer_y, spacer_z = self.params.spacer_pcb['size']

        x = (cap_numb - 1)*cap_spac + cap_diam + 2*spacer_x
        y = self.params.base_pcb['size'][1]
        z = self.params.back_plate['thickness']
        color = self.params.back_plate['color']

        # Create tap holes
        hole_diam = self.params.back_plate['hole_diameter']

        cap_hole_num = self.params.base_pcb['sandwich_hole_num']
        cap_hole_offset = self.params.base_pcb['sandwich_hole_offset']
        cap_hole_y_top =  0.5*y - cap_hole_offset
        cap_hole_y_bot = -0.5*y + cap_hole_offset
        cap_hole_y_pos = scipy.linspace(cap_hole_y_bot, cap_hole_y_top, cap_hole_num)


        hole_list = []
        for i in range(0,cap_numb):
            x_pos_left = 0.5*x - 0.5*spacer_x - i*cap_spac 
            x_pos_right = 0.5*x - 1.5*spacer_x - cap_diam - i*cap_spac 
                    
            for y_pos in cap_hole_y_pos:
                hole_left = x_pos_left, y_pos, hole_diam
                hole_right = x_pos_right, y_pos, hole_diam
                hole_list.append(hole_left)
                hole_list.append(hole_right)

        self.part = plate_w_holes(x,y,z, hole_list)
        self.part = Color(self.part,rgba=color)

# -----------------------------------------------------------------------------
if __name__ == '__main__':
    plate = BackPlate()
    prog = SCAD_Prog()
    prog.fn = 100
    prog.add(plate)
    prog.write('plate.scad')




