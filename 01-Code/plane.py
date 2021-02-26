#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Class plane:
===========+

  Models a plane downstream from the nuStorm production straight

  Version: 2.0                                  Date:25 February 2020
  Author: Paul Kyberd

  Version 2.1   remove the electron from consideration and do both neutrinos

  Version 2.0   Allow the x and y positions of the decaying muon to be off axis

  Version 1.0   Get the x, y position of the intersection of a neutrino trajectory
                with a plane at a distance sP (m) down stream of the end of the straight
                given the muonDecay instance


>>>>> this to modify 
  Class attributes:
  -----------------
  __MuonDecay: muon decay class
  --np       : numpy class
      
  Instance attributes:
  --------------------
  zPos: postion of plane downstream of the straight
  particleSpecies: type of particle for which this plane was created 
    
  Methods:
  --------
  Built-in methods __new__, __repr__ and __str__.
      __init__ : a plane instance
      __repr__ : One liner with call.
      __str__  : Dump of values of the plane

  Get/set methods:
    getzPos           : Returns the distance of the plane downstream of the straight
  
  General methods:
    findHitPosition      : finds (and stores?) the hit position of a particle with the plane

  Shortcomings: the decay position has x=y=0, so it is assumed here
                the length of the decay straight is put in by hand - not sure how to sort this out

"""

from copy import deepcopy
import math
import numpy as np
import matplotlib.pyplot as plt

    
class plane:

    __Debug  = False


#--------  "Built-in methods":
    def __init__(self, zPos=50.):

        self.zPos = zPos
        self.R=[]
        self.Energy=[]
        self.RLowCut = 0.0
        self.RHighCut = 5.0

#        self._TrcSpcCrd, self._P_e, self._P_nue, self._P_numu, self._RestFrame = self.CreateNeutrinos()
        
        return

    def __repr__(self):
        return "plane(zPos, particleSpecies)\n"\
        "          z is distance downstream of the end of the nuStorm Straight\n" \
        "          Particle Species is corresponding particle for the plane "


    def __str__(self):
        return "plane : z(m) = %g \r\n" \
                % (self.zPos)
    
    def addHitPosition(self, hit):

        self.R.append(hit[2])
        return

    def addHitE(self,hit):

        if hit[2] > self.RLowCut and hit[2] < self.RHighCut:
            self.Energy.append(hit[4])
        return

# Find the intercept of the particle with plane and store it along with the energy
    def findHitPosition(self, nuEvt):
#  Decay point information
        DecayPntX = nuEvt.getTraceSpaceCoord()[1]
        DecayPntY = nuEvt.getTraceSpaceCoord()[2]
        DecayPntZ = nuEvt.getTraceSpaceCoord()[3]

#  Now the information for both neutrinos
        eE = nuEvt.getnue4mmtm()[0]         # number
        pE = nuEvt.getnue4mmtm()[1]         # 3 vector
        eMu = nuEvt.getnumu4mmtm()[0]
        pMu = nuEvt.getnumu4mmtm()[1]

#  Distance to the plane
        deltaZ = self.zPos + 180.0 - DecayPntZ
        if self.__Debug: print ("path length is ", deltaZ)
#  Position of the nue hit               # need to check by hand - no test
        hitE=[]
        xPnt = (DecayPntX + pE[0]*deltaZ/pE[2])
        yPnt = (DecayPntY + pE[1]*deltaZ/pE[2])
        hitE.append(xPnt)                                 # x
        hitE.append(yPnt)                                 # y
        hitE.append(np.sqrt(xPnt*xPnt + yPnt*yPnt))       # R
        hitE.append(math.atan2(yPnt, xPnt))               # phi
        hitE.append(pE[0])                               # px
        hitE.append(pE[1])                               # py
        hitE.append(pE[2])                               # pz
        hitE.append(eE)                                   # E

        if self.__Debug: print (" hit: x, y, R, phi, E ", hitE[0], " ", hitE[1], " ", hitE[2], " ", hitE[3], " ", hitE[4])

#  Position of the numu hit               # need to check by hand - no test
        hitMu=[]
        xPnt = (DecayPntX + pMu[0]*deltaZ/pMu[2])
        yPnt = (DecayPntY + pMu[1]*deltaZ/pMu[2])
        hitMu.append(xPnt)                                 # x
        hitMu.append(yPnt)                                 # y
        hitMu.append(np.sqrt(xPnt*xPnt + yPnt*yPnt))       # R
        hitMu.append(math.atan2(yPnt, xPnt))               # phi
        hitMu.append(pMu[0])                               # px
        hitMu.append(pMu[1])                               # py
        hitMu.append(pMu[2])                               # pz
        hitMu.append(eMu)                                  # E


        if self.__Debug: print (" hit: x, y, R, phi, E ", hitMu[0], " ", hitMu[1], " ", hitMu[2], " ", hitMu[3], " ", hitMu[4])

        return hitE, hitMu

#.. Trace space coordinate generation:
    def getlongipos(self, Dcy):
        Pmu = self.getpmu()
        Emu = np.sqrt(Pmu**2 + \
                                              NeutrinoEventInstance.__mumass**2)
        v   = Pmu / Emu * NeutrinoEventInstance.__sol

        s   = v * Dcy.getLifetime()
        z   = s                      #.. limitation: muon trajectory along x=y=0
        
        return s, z


#--------  get/set methods:
    def getzPos(self):
        return self.zPos

    def getpmu(self):
        return deepcopy(self._pmu)

    def getTraceSpaceCoord(self):
        return deepcopy(self._TrcSpcCrd)
