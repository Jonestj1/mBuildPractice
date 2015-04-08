__author__ = 'Trev'


import mbuild as mb

class Ethane(mb.Compound):

    def __init__(self):
        super(Ethane, self).__init__()

        self.add(CH3(), 'methyl1')
        self.add(CH3(), 'methyl2')
        mb.equivalence_transform(self.methyl1, self.methyl1.up, self.methyl2.up)

class CH3(mb.Compound):

    def __init__(self):
        super(CH3, self).__init__()

        mb.load('ch3.pdb', compound=self, relative_to_module=self.__module__)
        mb.translate(self, -self.C[0])  # Move carbon to origin.

        port = mb.Port(anchor=self.C[0])
        self.add(port, label='up')
        mb.translate(self.up, [0, -0.07, 0])

m = CH3()
m.visualize(show_ports=True)
e = Ethane()
e.visualize()