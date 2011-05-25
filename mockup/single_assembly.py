from py2scad import *
from capillary import Capillary
from base_pcb import BasePCB
from spacer_pcb import SpacerPCB
from top_pcb import TopPCB
from back_plate import BackPlate
from standoff import Standoff
from fourforty import FourForty
from thumbscrew import ThumbScrew
import params

MM2INCH = 1/25.4


class SingleAssembly(object):
    
    def __init__(self,params=params): 
        self.params = params
        self.__make()

    def __make(self):
        # Create base_pcb
        self.base_pcb = BasePCB()
        base_x,base_y,base_z = self.params.base_pcb['size']

        # Create capillaries
        cap_temp = Capillary()
        cap_numb = self.params.base_pcb['capillary_number']
        cap_spac = self.params.base_pcb['capillary_spacing']
        cap_diam = self.params.capillary['diameter']
        self.capillary_list = []


        for i, pos_x in enumerate(self.base_pcb.cap_x_pos):
            z_pos = 0.5*cap_diam + 0.5*base_z
            cap = Translate(cap_temp.part,v=[pos_x,0,z_pos])
            self.capillary_list.append(cap)

        # Create spacers
        spacer_temp = SpacerPCB()
        spacer_x, spacer_y, spacer_z = self.params.spacer_pcb['size']
        self.spacer_list = []
        
        print 'spacer x-positions'
        print '-'*60
        for x_pos in self.base_pcb.spacer_x_pos:
            print 5.5 + x_pos*MM2INCH
            z_pos = 0.5*spacer_z + 0.5*base_z
            spacer = Translate(spacer_temp, v=[x_pos,0,z_pos])
            self.spacer_list.append(spacer)
        print 

        # Create top pcbs
        top_temp = TopPCB()
        top_x, top_y, top_z = self.params.top_pcb['size']
        self.top_list = []
        print 'capacitence pads x-posistion' 
        print '-'*60
        for x_pos in self.base_pcb.cap_x_pos:
            print 5.5 + x_pos*MM2INCH
            z_pos = 0.5*top_z + 0.5*base_z + spacer_z
            top = Translate(top_temp, v=[x_pos,0,z_pos])
            self.top_list.append(top)
        print

        # Create back plate
        self.back_plate = BackPlate()
        plate_thickness = self.params.back_plate['thickness'] 
        x_pos = 0.5*(self.base_pcb.cap_x_pos[0] + self.base_pcb.cap_x_pos[-1])
        z_pos = -0.5*plate_thickness - 0.5*base_z
        self.back_plate = Translate(self.back_plate,v=[x_pos, 0, z_pos])

        # Create standoffs
        standoff_height = self.params.standoff['height']

        standoff_temp = Standoff()
        self.standoff_list = []
        z_pos = -0.5*standoff_height - 0.5*base_z
        for x_pos, y_pos in self.base_pcb.mount_hole_xy:
            standoff = Translate(standoff_temp,v=(x_pos, y_pos, z_pos))
            self.standoff_list.append(standoff)

        # Create screws
        self.screw_list = []
        screw_temp = FourForty()
        z_pos = 0.5*base_z
        print 'mount hole x,y-positions'
        print '-'*60
        for x_pos, y_pos in self.base_pcb.mount_hole_xy:
            print 5.5 + x_pos*MM2INCH, 2.625 - y_pos*MM2INCH
            screw = Translate(screw_temp, v=(x_pos, y_pos, z_pos))
            self.screw_list.append(screw)
        print

        ##screw_temp = ThumbScrew()
        #screw_temp = FourForty()
        #z_pos = 0.5*base_z + spacer_z + top_z
        #for x_pos, y_pos, dummy in self.base_pcb.cap_holes:
        #    screw = Translate(screw_temp, v=(x_pos,y_pos,z_pos))
        #    self.screw_list.append(screw)
            

    def get_parts(self,explode = None):
        if explode is not None:
            # spacers
            v = 0,0,explode
            spacer_list = [Translate(obj,v=v) for obj in self.spacer_list]
            # capillaries
            v = 0,0,1.5*explode
            capillary_list = [Translate(obj,v=v) for obj in self.capillary_list]
            # top pcbs
            v = 0,0,2*explode
            top_list = [Translate(obj,v=v) for obj in self.top_list]
            # back plate
            v = 0,0,-explode
            back_plate = Translate(self.back_plate,v=v)
            #standoff
            v = 0,0,-explode
            standoff_list = [Translate(obj,v=v) for obj in self.standoff_list]
            v = 0,0, 3*explode
            screw_list = [Translate(obj,v=v) for obj in self.screw_list]
        else:
            spacer_list = self.spacer_list
            capillary_list = self.capillary_list
            top_list = self.top_list
            back_plate = self.back_plate
            standoff_list = self.standoff_list
            screw_list = self.screw_list

        parts = []
        parts.append(self.base_pcb)
        parts.extend(spacer_list)
        parts.extend(capillary_list)
        parts.extend(top_list)
        #parts.append(back_plate)
        #parts.extend(standoff_list)
        #parts.extend(screw_list)

        return parts


# -----------------------------------------------------------------------------
if __name__ == '__main__':
    #explode = 10 
    explode = 0 
    assem = SingleAssembly()
    prog = SCAD_Prog()
    prog.fn = 100
    prog.add(assem.get_parts(explode))
    prog.write('single_assembly.scad')





