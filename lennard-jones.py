# Week 1 Assigment 3
# Code to compute the value of the Lennard-Jones (LJ) potential for a pair of Argon atoms
# as a function of the separation between the atoms
#
# Author: Oliviero Andreussi
# 
# Variables: 
#   epsilon and sigma: LJ parmeters in atomic units
#   distance: distance between atoms in atomic units
#   ulj: LJ potential in atomic units
epsilon = 4.0e-4 # these are a.u.
sigma = 6 # also a.u.
distance = float(input('Specify the separation between the atoms (in a.u.): '))
ulj = 4*epsilon*(sigma/distance**12-sigma/distance**6)
print("The potential energy of two Argon atoms at a distance of %f a.u. is %f a.u." % (distance,ulj))
