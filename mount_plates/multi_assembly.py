from py2scad import *
import params
from single_assembly import SingleAssembly
from assembly_mount_plate import AssemblyMountPlate


class MultiAssembly(object):

    def __init__(self,params=params):
        self.params = params
        self.__make()

    def __make(self):
        num = self.params.multi_assembly['num']
        spacing = self.params.multi_assembly['spacing']
        single_assem = SingleAssembly()
        base_x, base_y, base_z = self.params.base_pcb['size']

        # Create measurement units
        unit_temp = Union(single_assem.get_parts())
        self.unit_list = []
        for i in range(0,num):
            x_pos = i*(base_x + spacing)
            unit = Translate(unit_temp, v=(x_pos, 0, 0))
            self.unit_list.append(unit)

        # Create mount plate
        thickness = self.params.assembly_mount_plate['thickness']
        standoff_height = self.params.standoff['height']
        self.mount_plate = AssemblyMountPlate()
        x_pos = 2*base_x + 2*spacing
        z_pos = -0.5*thickness - 0.5*base_z - standoff_height
        self.mount_plate = Translate(self.mount_plate,v=(x_pos, 0, z_pos))


    def get_parts(self, explode=None):

        parts = []
        if explode is not None:
            unit_list = self.unit_list
            mount_plate = self.mount_plate
        else:
            unit_list = self.unit_list
            mount_plate = self.mount_plate
        parts.extend(unit_list)
        parts.append(mount_plate)
        return parts

#------------------------------------------------------------------------------ 
if __name__ == '__main__':
    explode = None 
    assem = MultiAssembly()
    prog = SCAD_Prog()
    prog.fn = 100
    prog.add(assem.get_parts(explode))
    prog.write('multi_assembly.scad')




