#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test script for "NeutrinoEventInstance" class
=============================================

  Assumes that nuSim code is in path.

  Script starts by testing built in methods.  Then a soak test with a
  large number of decays is executed.  Finally a set of reference plots
  are generated.

"""

import MuonConst as muCnst
import NeutrinoEventInstance as nuEvtInst
import numpy as np
import matplotlib.pyplot as plt
import Simulation as Simu

mc = muCnst.MuonConst()

##! Start:
print("========  NeutrinoEventInstance: tests start  ========")

##! Create instance, test built-in methods:
NeutrinoEventInstanceTest = 1
print()
print("NeutrinoEventInstanceTest:", NeutrinoEventInstanceTest, " Test built-in methods.")
nuEI = nuEvtInst.NeutrinoEventInstance(5.)
print("    __str__:", nuEI)
print("    --repr__", repr(nuEI))

##! Test get/set methods:
NeutrinoEventInstanceTest = 2
print()
print("NeutrinoEventInstanceTest:", NeutrinoEventInstanceTest, \
      "Test get/set methods.")
print("    Muon momentum (GeV):", nuEI.getpmu())

##! Test methods by which neutrino-creation event is generated:
NeutrinoEventInstanceTest = 3
print()
print("NeutrinoEventInstanceTest:", NeutrinoEventInstanceTest, \
      "Test methods by which neutrino-creation event is generated.")
x = nuEI.CreateNeutrinos()
print("    Neutrino event: trace-space coordinates of muon at decay, P_e, P_nue, P_numu:", x)
del nuEI

##! Soak test:
NeutrinoEventInstanceTest = 4
print()
print("NeutrinoEventInstanceTest:", NeutrinoEventInstanceTest, \
      "soak test.")
nuEI = []
for i in range(40000):
    nuEI.append(nuEvtInst.NeutrinoEventInstance(5.))
for i in range(5):
    print("    nuEI[i]:", nuEI[i])

##! Plot result of soak test:
NeutrinoEventInstanceTest = 5
print()
print("NeutrinoEventInstanceTest:", NeutrinoEventInstanceTest, \
      "plots from soak test.")

s       = np.array([])
Ee      = np.array([])
Enue    = np.array([])
Enumu   = np.array([])
tane    = np.array([])
tannue  = np.array([])
tannumu = np.array([])
Rnue    = np.array([])
Rnumu   = np.array([])
CutEnue = np.array([])
CutEnumu= np.array([])

for nuEvt in nuEI:
    s     = np.append(s,     nuEvt.getTraceSpaceCoord()[0])
    Ee    = np.append(Ee,    nuEvt.gete4mmtm()[0])
    Enue  = np.append(Enue,  nuEvt.getnue4mmtm()[0])
    Enumu = np.append(Enumu, nuEvt.getnumu4mmtm()[0])
    
    pt_e    = np.sqrt(nuEvt.gete4mmtm()[1][0]**2 + nuEvt.gete4mmtm()[1][1]**2)
    pt_nue  = np.sqrt(nuEvt.getnue4mmtm()[1][0]**2 + nuEvt.getnue4mmtm()[1][1]**2)
    pt_numu = np.sqrt(nuEvt.getnumu4mmtm()[1][0]**2 + nuEvt.getnumu4mmtm()[1][1]**2)

    tane    = np.append(tane,    (pt_e/nuEvt.gete4mmtm()[1][2]) )
    tannue  = np.append(tannue,  (pt_nue/nuEvt.getnue4mmtm()[1][2]) )
    tannumu = np.append(tannumu, (pt_numu/nuEvt.getnumu4mmtm()[1][2]) )

#-- Lifetime distribution:
n, bins, patches = plt.hist(s, bins=50, color='y', log=True)
plt.xlabel('s (m)')
plt.ylabel('Entries')
plt.title('s distribution')
# add a 'best fit' line
l = 1./(mc.lifetime      ()*mc.SoL())
y = n[0]*np.exp(-l*bins)
plt.plot(bins, y, '-', color='b')
plt.show()
plt.close()

#-- Energy distributions:
n, bins, patches = plt.hist(Ee, bins=50, color='y', range=(0.,5.0))
plt.xlabel('Energy (GeV)')
plt.ylabel('Frequency')
plt.title('Electron energy distribution')
plt.show()
plt.close()

n, bins, patches = plt.hist(Enue, bins=50, color='y', range=(0.,5.))
plt.xlabel('Energy (GeV)')
plt.ylabel('Frequency')
plt.title('Electron-neutrino energy distribution')
plt.show()
plt.close()

n, bins, patches = plt.hist(Enumu, bins=50, color='y', range=(0.,5.))
plt.xlabel('Energy (GeV)')
plt.ylabel('Frequency')
plt.title('Muon-neutrino energy distribution')
plt.show()
plt.close()

##! Complete:
print()
print("========  NeutrinoEventInstance: tests complete  ========")
