import scipy
from py2scad import *
import params

class SpacerPCB(object):

    def __init__(self,params=params):
        self.params = params
        self.__make()

    def __str__(self):
        return self.part.__str__()

    def __make(self):
        x,y,z = self.params.spacer_pcb['size']
        color = self.params.spacer_pcb['color']

        hole_num = self.params.base_pcb['sandwich_hole_num']
        hole_diam = self.params.base_pcb['sandwich_hole_diam']
        hole_offset = self.params.base_pcb['sandwich_hole_offset']
        hole_y_top = 0.5*y - hole_offset
        hole_y_bot = -0.5*y + hole_offset
        hole_y_pos = scipy.linspace(hole_y_bot, hole_y_top, hole_num)
        hole_list = []
        for y_pos in hole_y_pos: 
            hole_list.append((0,y_pos,hole_diam))

        pcb = plate_w_holes(x,y,z,hole_list)
        pcb = Color(pcb, rgba=color)
        self.part = pcb


# -----------------------------------------------------------------------------
if __name__ == '__main__':
    pcb = SpacerPCB()
    prog = SCAD_Prog()
    prog.fn = 100
    prog.add(pcb)
    prog.write('spacer_pcb.scad')

