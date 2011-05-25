import scipy
from py2scad import *
import params

MM2INCH = 1.0/25.4

class TopPCB(object):

    def __init__(self,params=params):
        self.params = params
        self.__make()

    def __str__(self):
        return self.part.__str__()

    def __make(self):
        x,y,z = self.params.top_pcb['size']
        #print 'top pcb size', (x*MM2INCH,y*MM2INCH,z*MM2INCH)
        color = self.params.top_pcb['color']

        cap_diam = self.params.capillary['diameter']
        cap_tol = self.params.base_pcb['capillary_tolerance']
        spacer_x, spacer_y, spacer_z = self.params.spacer_pcb['size']

        hole_num = self.params.base_pcb['sandwich_hole_num']
        hole_diam = self.params.base_pcb['sandwich_hole_diam']
        hole_offset = self.params.base_pcb['sandwich_hole_offset']
        hole_y_top = 0.5*y - hole_offset
        hole_y_bot = -0.5*y + hole_offset

        hole_list = []
        hole_y_pos = scipy.linspace(hole_y_bot, hole_y_top, hole_num)
        for y_pos in hole_y_pos: 
            for i in (-1,1):
                pos_x = i*(0.5*cap_diam + 0.5*cap_tol + 0.5*spacer_x) 
                print 'hole x pos', MM2INCH*(pos_x + 0.5*x) + 1.0
                hole_list.append((pos_x,y_pos,hole_diam))
        self.part = plate_w_holes(x,y,z,hole_list)
        self.part = Color(self.part,rgba=color)

# -----------------------------------------------------------------------------
if __name__ == '__main__':
    pcb = TopPCB()
    prog = SCAD_Prog()
    prog.fn = 100
    prog.add(pcb)
    prog.write('top_pcb.scad')



