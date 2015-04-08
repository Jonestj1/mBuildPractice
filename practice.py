__author__ = 'Trev'

import mbuild as mb

class Methane(mb.Compound):

    def __init__(self):
        super(Methane, self).__init__()
        carbon = mb.Atom(name='C')
        self.add(carbon)

        hydrogen = mb.Atom(name='H', pos=[0.11, 0, 0])
        self.add(hydrogen, label='HC[$]')

        hydrogen = mb.Atom(name='H', pos=[-0.11, 0, 0])
        self.add(hydrogen, label='HC[$]')
        hydrogen = mb.Atom(name='H', pos=[0, 0.11, 0])
        self.add(hydrogen, label='HC[$]')
        hydrogen = mb.Atom(name='H', pos=[0, -0.11, 0])
        self.add(hydrogen, label='HC[$]')

        ch_bond = mb.Bond(self.atoms[0], self.HC[0])
        self.add(ch_bond)
        ch_bond = mb.Bond(self.atoms[0], self.HC[1])
        self.add(ch_bond)
        ch_bond = mb.Bond(self.atoms[0], self.HC[2])
        self.add(ch_bond)
        ch_bond = mb.Bond(self.atoms[0], self.HC[3])
        self.add(ch_bond)

if __name__ == "__main__":
    methane = Methane()
    methane.visualize()