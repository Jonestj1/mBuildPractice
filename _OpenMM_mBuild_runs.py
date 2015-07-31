__author__ = 'jonestj1'
from simtk.openmm.app import *
from simtk.openmm import *
from simtk.unit import *
from sys import stdout

gro = GromacsGroFile('/Users/jonestj1/mBuildPractice/0_0_alkane_monolayer.gro')
top = GromacsTopFile('/Users/jonestj1/mBuildPractice/0_0_alkane_monolayer.top', unitCellDimensions=gro.getUnitCellDimensions(),
                     includeDir='/Users/jonestj1/mBuildPractice/')

system = top.createSystem(nonbondedMethod=PME, nonbondedCutoff=1*nanometer,
                          constraints=HBonds)
integrator = LangevinIntegrator(300*kelvin, .1/picosecond, 0.0002*picoseconds)

# Fix Si atom positions in place in betacristobilate
force = CustomExternalForce("k*((x-x0)^2+(y-y0)^2+(z-z0)^2)")
force.addGlobalParameter("k", 5.0)
force.addPerParticleParameter("x0")
force.addPerParticleParameter("y0")
force.addPerParticleParameter("z0")
for index, atom_cord in enumerate(gro.positions):
    if gro.atomNames[index] == 'Si' and atom_cord[2] == 0*nanometers:
        count += 1
        force.addParticle(index, atom_cord.value_in_unit(nanometers))
system.addForce(force)

# # Fix Si atom positions in place in betacristobalite
# # First compute the system mass
# sum = 0*dalton
# for particle in range(system.getNumParticles()):
#     sum += system.getParticleMass(particle)
# total_mass = sum
# for index, atom_cord in enumerate(gro.positions):
#     if gro.atomNames[index] in ('SI', 'O') and atom_cord[2] < 0.06 * nanometers:
#         system.setParticleMass(index, 0*dalton)

# # Apply Oplsaa
# custom_force = CustomNonbondedForce("4*epsilon*((sigma/r)^12-(sigma/r)^6); sigma=sqrt(sigma1*sigma2); epsilon=sqrt(epsilon1*epsilon2)")
# custom_force.addPerParticleParameter("sigma")
# custom_force.addPerParticleParameter("epsilon")
# nonbonded_force = system.getForce(0)
# for particle in range(system.getNumParticles()):
#     parameters = nonbonded_force.getParticleParameters(particle)
#     custom_force.addParticle([parameters[1], parameters[2]])
#     nonbonded_force.setParticleParameters(particle, parameters[0], 0, 0)
# print('custom:', custom_force.getParticleParameters(0))
# print('actual:', nonbonded_force.getParticleParameters(0))
# system.addForce(custom_force)


simulation = Simulation(top.topology, system, integrator)

simulation.context.setPositions(gro.positions)
# simulation.minimizeEnergy(maxIterations=50000)
simulation.context.getState(getPositions=True)
simulation.reporters.append(PDBReporter('output.pdb', 1))
simulation.reporters.append(StateDataReporter(stdout, 1, step=True,
                                              potentialEnergy=True,
                                              temperature=True,
                                              separator=',\t'))
print('begining steps')
simulation.step(20)


"""
HBonds
[<simtk.openmm.openmm.NonbondedForce; proxy of <Swig Object of type 'OpenMM::NonbondedForce *' at 0x1045c26c0> >,
<simtk.openmm.openmm.HarmonicAngleForce; proxy of <Swig Object of type 'OpenMM::HarmonicAngleForce *' at 0x1045c2600> >,
<simtk.openmm.openmm.CMMotionRemover; proxy of <Swig Object of type 'OpenMM::CMMotionRemover *' at 0x1045c2750> >]
"""

"""
AllBonds
[<simtk.openmm.openmm.NonbondedForce; proxy of <Swig Object of type 'OpenMM::NonbondedForce *' at 0x1044bb6c0> >,
<simtk.openmm.openmm.HarmonicBondForce; proxy of <Swig Object of type 'OpenMM::HarmonicBondForce *' at 0x1044bb600> >,
<simtk.openmm.openmm.HarmonicAngleForce; proxy of <Swig Object of type 'OpenMM::HarmonicAngleForce *' at 0x1044bb7e0> >,
<simtk.openmm.openmm.CMMotionRemover; proxy of <Swig Object of type 'OpenMM::CMMotionRemover *' at 0x1044bb750> >]
"""