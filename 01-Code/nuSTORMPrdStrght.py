#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Class nuSTORMPrdStrght:
=======================

  Defines the parameters of the nuSTORM production straight and
  contains methods for the simulation of the decay-straight optics.
  
  First implementation contains first order simulation in which
  s=z and representative values of emittance and beta are simulated
  for alpha=0 (see nuSIM-2021-01).

  Class attributes:
  -----------------
  __instance : Set on creation of first (and only) instance.
      
  Instance attributes:
  --------------------
  _filename        = Filename, includin path, to cls file containing
                     nuSTORM production straight specification
  _PrdStrghtParams = Pandas dataframe containing specification in 
                     _filename
  _Circumference   = Ring circumference (m)
  _ProdStrghtLen   = Production straight length (m)
  _pAcc            = Momentum acceptance (%)
  _epsilon         = Representative emittance/acceptance (pi mm rad)
  _beta            = Representative beta function (mm)
    
  Methods:
  --------
  Built-in methods __new__, __repr__ and __str__.
      __new__ : Creates singleton class and prints version and values
                of decay-straight parameters used.
      __repr__: One liner with call.
      __str__ : Dump of constants

  Get/set methods:
      CdVrsn()     : Returns code version number.
      Circumference: Get circumference (m)
      ProdStrghtLen: Get production straight length (m)
      pAcc         : Get momentum acceptance (%)
      epsilon      : Get acceptance/emittance (pi mm rad)
      beta         : Get beta function (mm)

  Generation, calcution methods and utilities:
      GenerateMmtm : Generates momentum centred on p0 (input float).
                     Parabolic distribution generated.
      Calculatez   : Calculate z of decay given s, p and production-straight
                     parameters.  **This version: z=s** (m)
      GenerateTrans: Generate transverse phase space (x, y, xp, yp) given
                     representative emittance and beta.  Parabolic distributions
                     generated.
      getParabolic : Generates a parabolic distributed random number from
                     -p1 to p1 (p1 input)
      getProdStraighParams: Read csv file and generate Pandas dataframe
      printParams  : Print all paramters

  
Created on Thu 21Feb21. Version history:
----------------------------------------
 1.0: 21Feb21: First implementation

@author: kennethlong
"""

import pandas as pnds
import numpy as np
from copy import deepcopy
from Simulation import *

class nuSTORMPrdStrght(object):
    __instance = None

#--------  "Built-in methods":
    def __new__(cls, filename):
        if cls.__instance is None:
            #print('nuSTORMPrdStrght.__new__: creating the nuSTORMPrdStrght object')
            cls.__instance = super(nuSTORMPrdStrght, cls).__new__(cls)

            cls._filename        = filename
            cls._PrdStrghtParams = cls.GetProdStraightParams(filename)
            cls._Circumference   = cls._PrdStrghtParams.iat[0,2]
            cls._ProdStrghtLen   = cls._PrdStrghtParams.iat[1,2]
            cls._pAcc            = cls._PrdStrghtParams.iat[2,2] / 100.
            cls._epsilon         = cls._PrdStrghtParams.iat[3,2]
            cls._beta            = cls._PrdStrghtParams.iat[4,2]
            
        return cls.__instance

    def __repr__(self):
        return "nuSTORMPrdStrght()"

    def __str__(self):
        return "nuSTORMPrdStrght: version=%g, circumference=%g m, length of production straight=%g," \
               " momentum acceptance=%g%%, transverse acceptance=%g pi mm rad, beta=%g mm." % \
               (self.CdVrsn(), self.Circumference(), self.ProdStrghtLen(), self.pAcc(), self.epsilon(), self.beta())

#--------  Simulation methods:
    def GenerateMmtm(self,p0):
        p = -99.
        dp = p0 * self._pAcc / 2.
        p  = p0 + nuSTORMPrdStrght.getParabolic(dp)
        return p

    def Calculatez(self,s):
        return s

    def GenerateTrans(self,s):
        r  = np.sqrt(self._epsilon*self._beta) / 1000.
        rp = np.sqrt(self._epsilon/self._beta)
        x  = nuSTORMPrdStrght.getParabolic(r)
        y  = nuSTORMPrdStrght.getParabolic(r)
        xp = nuSTORMPrdStrght.getParabolic(rp)
        yp = nuSTORMPrdStrght.getParabolic(rp)
        return x, y, xp, yp

    def getParabolic(p1):
        ran = getRandom()
        a = np.array( [ 1., 0., (-3.*p1*p1), (2.*p1*p1*p1*(2.*ran - 1.)) ] )
        r = np.roots(a)
        isol = 0
        for ri in r:
            if not isinstance(ri, complex):
                if ri >= -p1:
                    if ri <= p1:
                        isol += 1
                        p = ri
        if isol != 1:
            raiseException("nuSTORMPrdStrght.getParabolic; p multiply defined")
        return p

#--------  I/o methods:
    def GetProdStraightParams(_filename):
        PrdStrghtParams = pnds.read_csv(_filename)
        return PrdStrghtParams
    
#--------  "Get methods" only; version, reference, and constants
#.. Methods believed to be self documenting(!)

    def CdVrsn(self):
        return 1.0

    def Circumference(self):        
        return deepcopy(self._Circumference)

    def ProdStrghtLen(self):        
        return deepcopy(self._ProdStrghtLen)

    def pAcc(self):        
        return deepcopy(self._pAcc)

    def epsilon(self):        
        return deepcopy(self._epsilon)

    def beta(self):        
        return deepcopy(self._beta)

    def printParams(self):
        print(self._PrdStrghtParams)
