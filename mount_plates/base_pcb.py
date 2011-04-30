import scipy
from py2scad import *
import params

class BasePCB(object):

    def __init__(self, params=params):
        self.params = params
        self.__make()

    def __str__(self):
        return self.part.__str__()

    def __make(self):
        # Create base pcb and add mount holes
        x,y,z = self.params.base_pcb['size']
        color = self.params.base_pcb['color']
        mount_hole_diam = self.params.base_pcb['mount_hole_diam']
        mount_hole_offset = self.params.base_pcb['mount_hole_offset']
        hole_list = []
        self.mount_hole_xy = []
        for i in (-1,1):
            for j in (-1,1):
                mount_hole_x = i*(0.5*x - mount_hole_offset)
                mount_hole_y = j*(0.5*y - mount_hole_offset)
                mount_hole = (mount_hole_x, mount_hole_y, mount_hole_diam)
                hole_list.append(mount_hole)
                self.mount_hole_xy.append((mount_hole_x, mount_hole_y))

        # Create holes for mounting capillaries
        cap_numb = self.params.base_pcb['capillary_number']
        cap_spac = self.params.base_pcb['capillary_spacing']
        cap_pad = self.params.base_pcb['capillary_pad_right']
        cap_diam = self.params.capillary['diameter']
        spacer_x, spacer_y, spacer_z = self.params.spacer_pcb['size']

        cap_hole_num = self.params.base_pcb['sandwich_hole_num']
        cap_hole_diam = self.params.base_pcb['sandwich_hole_diam']
        cap_hole_offset = self.params.base_pcb['sandwich_hole_offset']
        cap_hole_y_top =  0.5*y - cap_hole_offset
        cap_hole_y_bot = -0.5*y + cap_hole_offset
        cap_hole_y_pos = scipy.linspace(cap_hole_y_bot, cap_hole_y_top, cap_hole_num)

        self.cap_x_pos = []
        self.spacer_x_pos = []
        self.cap_holes = []

        for i in range(0,cap_numb):
            x_pos = 0.5*x - 0.5*cap_spac - i*cap_spac - cap_pad 
            self.cap_x_pos.append(x_pos)

            x_pos_left = x_pos - 0.5*cap_diam - 0.5*spacer_x
            x_pos_right = x_pos + 0.5*cap_diam + 0.5*spacer_x 
            self.spacer_x_pos.append(x_pos_left)
            self.spacer_x_pos.append(x_pos_right)
                    
            for y_pos in cap_hole_y_pos:
                hole_left = x_pos_left, y_pos, cap_hole_diam
                hole_right = x_pos_right, y_pos, cap_hole_diam
                self.cap_holes.append(hole_left)
                self.cap_holes.append(hole_right)
                hole_list.append(hole_left)
                hole_list.append(hole_right)
                

        pcb = plate_w_holes(x,y,z,hole_list)
        pcb = Color(pcb, rgba=color)


        self.part = pcb


# -----------------------------------------------------------------------------

if __name__ == '__main__':
    base_pcb = BasePCB()
    prog = SCAD_Prog()
    prog.fn = 100
    prog.add(base_pcb.part)
    prog.write('base_pcb')
