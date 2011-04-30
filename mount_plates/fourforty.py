from py2scad import *
import params

class FourForty(object):

    def __init__(self,params=params):
        self.params = params
        self.__make()

    def __str__(self):
        return self.part.__str__()

    def __make(self):
        color = self.params.fourforty['color']
        shaft_diameter = self.params.fourforty['shaft_diameter']
        shaft_length = self.params.fourforty['shaft_length']
        head_diameter = self.params.fourforty['head_diameter']
        head_thickness = self.params.fourforty['head_thickness']

        shaft_radius = 0.5*shaft_diameter
        shaft = Cylinder(h=shaft_length, r1=shaft_radius, r2=shaft_radius)
        head_radius = 0.5*head_diameter
        head = Cylinder(h=head_thickness, r1=head_radius, r2=head_radius)

        shaft = Translate(shaft,v=[0,0,-0.5*shaft_length])
        head = Translate(head,v=[0,0,0.5*head_thickness])

        part = Union([shaft,head])
        part = Color(part,rgba=color)
        self.part = part

# -----------------------------------------------------------------------------
if __name__ == '__main__':
    part = FourForty()
    prog = SCAD_Prog()
    prog.fn = 100
    prog.add(part)
    prog.write('fourforty.scad')


