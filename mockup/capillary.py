from py2scad import *
import params

class Capillary(object):

    def __init__(self, params=params):
        self.params = params
        self.__make()

    def __str__(self):
        return self.part.__str__()

    def __make(self):
        length = self.params.capillary['length']
        radius = 0.5*self.params.capillary['diameter']
        color = self.params.capillary['color']
        self.part = Cylinder(h=length, r1=radius, r2=radius)
        self.part = Color(self.part,color)
        self.part = Rotate(self.part,a=90,v=[1,0,0])


# -----------------------------------------------------------------------------
if __name__ == '__main__':
    cap = Capillary()
    prog = SCAD_Prog()
    prog.fn = 100
    prog.add(cap.part)
    prog.write('capillary.scad')


