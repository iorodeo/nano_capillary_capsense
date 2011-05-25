from py2scad import *
import params
from base_pcb import BasePCB

class AssemblyMountPlate(object):

    def __init__(self,params=params):
        self.params = params
        self.__make()

    def __str__(self):
        return self.part.__str__()

    def __make(self):

        # Get plate parameters
        margin_x = self.params.assembly_mount_plate['margin_x']
        margin_y = self.params.assembly_mount_plate['margin_y']
        thickness = self.params.assembly_mount_plate['thickness']
        num = self.params.multi_assembly['num']
        spacing = self.params.multi_assembly['spacing']
        base_x,base_y,base_z = self.params.base_pcb['size']
        plate_x = num*(base_x + spacing) + 2*margin_x
        plate_y = base_y + 2*margin_y
        plate_z = thickness
        print plate_x, plate_y, plate_z

        # Add fourforty tap holes
        fourforty_diam = self.params.assembly_mount_plate['fourforty_tap_diam']
        hole_list = []
        base_pcb = BasePCB()
        
        for i in range(0,num):
            for x_pos, y_pos in base_pcb.mount_hole_xy:
                x_pos = (x_pos - 2*base_x - 2*spacing) + i*(base_x + spacing)
                hole = (x_pos, y_pos, fourforty_diam)
                hole_list.append(hole)

        # Add 1/4-20 through holes
        qtr_twenty_offset = self.params.assembly_mount_plate['qtr_twenty_offset']
        qtr_twenty_diam = self.params.assembly_mount_plate['qtr_twenty_thru_diam']
        for i in (-1,1):
            for j in (-1,1):
                x_pos = i*(0.5*plate_x - qtr_twenty_offset)
                y_pos = j*(0.5*plate_y - qtr_twenty_offset)
                hole = (x_pos, y_pos, qtr_twenty_diam)
                hole_list.append(hole)

        plate = plate_w_holes(plate_x, plate_y, plate_z, hole_list)
        self.part = plate

# -----------------------------------------------------------------------------
if __name__ == '__main__':
    part = AssemblyMountPlate()
    prog = SCAD_Prog()
    prog.fn = 100
    prog.add(part)
    prog.write('assembly_mount_plate.scad')
