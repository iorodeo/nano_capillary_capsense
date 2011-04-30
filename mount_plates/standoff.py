from py2scad import *
import params

class Standoff(object):

    def __init__(self,params=params):
        self.params = params
        self.__make()

    def __str__(self):
        return self.part.__str__()

    def __make(self):
        color = self.params.standoff['color']
        diam = self.params.standoff['diameter']
        height = self.params.standoff['height']
        hole_diam = self.params.standoff['hole_diameter']
        part = Cylinder(h=height,r1=0.5*diam, r2=0.5*diam)
        cut_cyl = Cylinder(h= 2*height, r1=0.5*hole_diam, r2=0.5*hole_diam)
        part = Difference([part, cut_cyl])
        part = Color(part,rgba=color)
        self.part = part

# -----------------------------------------------------------------------------
if __name__ == '__main__':
    standoff = Standoff()
    prog = SCAD_Prog()
    prog.fn = 100
    prog.add(standoff)
    prog.write('standoff.scad')




