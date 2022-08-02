#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test script for updated "plane2" class ...
==========================================

  plane2.py -- set "relative" path to code

"""

import plane as plane
import NeutrinoEventInstance as nuEvtInst
import traceSpace as trSp
import histoManager
import numpy as np
import sys, os
from statistics import mean


class planeTst():

  __DBG = False
  __shrtRun = False

  histDir = "/Users/paulkyberd/work/nuStudy"
  texDir = "/Users/paulkyberd/work/nuStudy/testing.tex"

  hm = histoManager.histoManager()

  testFails = 0
  typPnt = 1

  hm = histoManager.histoManager()

#   Production straight
  hTitle = "PS - numu: px"
  hBins  = 100
  hLower = -0.2
  hUpper = 0.2
  hpxnumuPS = hm.book(hTitle, hBins, hLower, hUpper)
  hTitle = "PS - numu: py"
  hLower = -0.2
  hUpper = 0.2
  hpynumuPS = hm.book(hTitle, hBins, hLower, hUpper)
  hTitle = "PS - numu: pz"
  hLower = -0.1
  hUpper = 3.2
  hpznumuPS = hm.book(hTitle, hBins, hLower, hUpper)
  hTitle = "PS - nue: px"
  hLower = -0.2
  hUpper = 0.2
  hpxnuePS = hm.book(hTitle, hBins, hLower, hUpper)
  hTitle = "PS - nue: py"
  hLower = -0.2
  hUpper = 0.2
  hpynuePS = hm.book(hTitle, hBins, hLower, hUpper)
  hTitle = "PS - nue: pz"
  hLower = -0.1
  hUpper = 3.2
  hpznuePS = hm.book(hTitle, hBins, hLower, hUpper)
  hTitle = "PS - mu: px"
  hLower = -0.2
  hUpper = 0.2
  hpxmuPS = hm.book(hTitle, hBins, hLower, hUpper)
  hTitle = "PS - mu: py"
  hLower = -0.2
  hUpper = 0.2
  hpymuPS = hm.book(hTitle, hBins, hLower, hUpper)
  hTitle = "PS - mu: pz"
  hLower = 2.5
  hUpper = 3.5
  hpzmuPS = hm.book(hTitle, hBins, hLower, hUpper)
  hTitle = "PS - muon decay: s"
  hLower = 300.0
  hUpper = 6000.0
  hmusPS = hm.book(hTitle, hBins, hLower, hUpper)
  hTitle = "PS - muon decay: x full"
  hLower = -10.0
  hUpper = 90.0
  hmuxFullPS = hm.book(hTitle, hBins, hLower, hUpper)
  hTitle = "PS - muon decay: x low"
  hLower = -1.0
  hUpper = 1.0
  hmuxLowPS = hm.book(hTitle, hBins, hLower, hUpper)
  hTitle = "PS - muon decay: x high"
  hLower = 80.0
  hUpper = 82.0
  hmuxHiPS = hm.book(hTitle, hBins, hLower, hUpper)
  hTitle = "PS - muon decay: y"
  hLower = -1.0
  hUpper = 1.0
  hmuyPS = hm.book(hTitle, hBins, hLower, hUpper)
  hTitle = "PS - muon decay: z"
  hLower = -50.0
  hUpper = 300.0
  hmuzPS = hm.book(hTitle, hBins, hLower, hUpper)

#   Return Straight
  hTitle = "RS - numu: px"
  hBins  = 100
  hLower = -0.2
  hUpper = 0.2
  hpxnumuRS = hm.book(hTitle, hBins, hLower, hUpper)
  hTitle = "RS - numu: py"
  hLower = -0.2
  hUpper = 0.2
  hpynumuRS = hm.book(hTitle, hBins, hLower, hUpper)
  hTitle = "RS - numu: pz"
  hLower = -3.2
  hUpper = 0.8
  hpznumuRS = hm.book(hTitle, hBins, hLower, hUpper)
  hLower = -0.2
  hUpper = 0.2
  hTitle = "RS - nue: px"
  hpxnueRS = hm.book(hTitle, hBins, hLower, hUpper)
  hTitle = "RS - nue: py"
  hpynueRS = hm.book(hTitle, hBins, hLower, hUpper)
  hLower = -3.2
  hUpper = 0.8
  hTitle = "RS - nue: pz"
  hpznueRS = hm.book(hTitle, hBins, hLower, hUpper)
  hTitle = "RS - mu: px"
  hLower = -0.2
  hUpper = 0.2
  hpxmuRS = hm.book(hTitle, hBins, hLower, hUpper)
  hTitle = "RS - mu: py"
  hLower = -0.2
  hUpper = 0.2
  hpymuRS = hm.book(hTitle, hBins, hLower, hUpper)
  hTitle = "RS - mu: pz"
  hLower = -3.5
  hUpper = 0.8
  hpzmuRS = hm.book(hTitle, hBins, hLower, hUpper)
  hTitle = "RS - muon decay: s"
  hLower = 300.0
  hUpper = 6000.0
  hmusRS = hm.book(hTitle, hBins, hLower, hUpper)
  hTitle = "RS - muon decay: x full"
  hLower = -10.0
  hUpper = 90.0
  hmuxFullRS = hm.book(hTitle, hBins, hLower, hUpper)
  hTitle = "RS - muon decay: x low"
  hLower = -1.0
  hUpper = 1.0
  hmuxLowRS = hm.book(hTitle, hBins, hLower, hUpper)
  hTitle = "RS - muon decay: x high"
  hLower = 80.0
  hUpper = 82.0
  hmuxHiRS = hm.book(hTitle, hBins, hLower, hUpper)
  hTitle = "RS - muon decay: y"
  hLower = -1.0
  hUpper = 1.0
  hmuyRS = hm.book(hTitle, hBins, hLower, hUpper)
  hTitle = "RS - muon decay: z"
  hLower = -50.0
  hUpper = 300.0
  hmuzRS = hm.book(hTitle, hBins, hLower, hUpper)

#   Top arc

  hTitle = "TA - numu: px"
  hBins  = 100
  hLower = -0.8
  hUpper = 3.2
  hpxnumuTA = hm.book(hTitle, hBins, hLower, hUpper)
  hTitle = "TA - numu: py"
  hLower = -0.2
  hUpper = 0.2
  hpynumuTA = hm.book(hTitle, hBins, hLower, hUpper)
  hTitle = "TA - numu: pz"
  hLower = -3.2
  hUpper = 3.2
  hpznumuTA = hm.book(hTitle, hBins, hLower, hUpper)
  hLower = -0.8
  hUpper = 3.2
  hTitle = "TA - nue: px"
  hpxnueTA = hm.book(hTitle, hBins, hLower, hUpper)
  hLower = -0.8
  hUpper = 3.2
  hTitle = "TA - nue: py"
  hpynueTA = hm.book(hTitle, hBins, hLower, hUpper)
  hLower = -4.0
  hUpper = 4.0
  hTitle = "TA - nue: pz"
  hpznueTA = hm.book(hTitle, hBins, hLower, hUpper)
  hTitle = "TA - mu: px"
  hLower = -3.2
  hUpper = 3.2
  hpxmuTA = hm.book(hTitle, hBins, hLower, hUpper)
  hTitle = "TA - mu: py"
  hLower = -0.2
  hUpper = 0.2
  hpymuTA = hm.book(hTitle, hBins, hLower, hUpper)
  hTitle = "TA - mu: pz"
  hLower = -4.0
  hUpper = 4.0
  hpzmuTA = hm.book(hTitle, hBins, hLower, hUpper)
  hTitle = "TA - muon decay: s"
  hLower = 300.0
  hUpper = 6000.0
  hmusTA = hm.book(hTitle, hBins, hLower, hUpper)
  hTitle = "TA - muon decay: x full"
  hLower = -10.0
  hUpper = 90.0
  hmuxFullTA = hm.book(hTitle, hBins, hLower, hUpper)
  hTitle = "TA - muon decay: x low"
  hLower = -1.0
  hUpper = 1.0
  hmuxLowTA = hm.book(hTitle, hBins, hLower, hUpper)
  hTitle = "TA - muon decay: x high"
  hLower = 80.0
  hUpper = 82.0
  hmuxHiTA = hm.book(hTitle, hBins, hLower, hUpper)
  hTitle = "TA - muon decay: y"
  hLower = -1.0
  hUpper = 1.0
  hmuyTA = hm.book(hTitle, hBins, hLower, hUpper)
  hTitle = "TA - muon decay: z"
  hLower = -50.0
  hUpper = 300.0
  hmuzTA = hm.book(hTitle, hBins, hLower, hUpper)

#   Bottom arc
  hTitle = "BA - numu: px"
  hBins  = 100
  hLower = -3.2
  hUpper = 0.8
  hpxnumuBA = hm.book(hTitle, hBins, hLower, hUpper)
  hTitle = "BA - numu: py"
  hLower = -0.2
  hUpper = 0.2
  hpynumuBA = hm.book(hTitle, hBins, hLower, hUpper)
  hTitle = "BA - numu: pz"
  hLower = -3.2
  hUpper = 3.2
  hpznumuBA = hm.book(hTitle, hBins, hLower, hUpper)
  hLower = -3.2
  hUpper = 0.8
  hTitle = "BA - nue: px"
  hpxnueBA = hm.book(hTitle, hBins, hLower, hUpper)
  hLower = -0.2
  hUpper = 0.2
  hTitle = "BA - nue: py"
  hpynueBA = hm.book(hTitle, hBins, hLower, hUpper)
  hLower = -4.0
  hUpper = 4.0
  hTitle = "BA - nue: pz"
  hpznueBA = hm.book(hTitle, hBins, hLower, hUpper)
  hTitle = "BA - mu: px"
  hLower = -3.2
  hUpper = 0.8
  hpxmuBA = hm.book(hTitle, hBins, hLower, hUpper)
  hTitle = "BA - mu: py"
  hLower = -0.2
  hUpper = 0.2
  hpymuBA = hm.book(hTitle, hBins, hLower, hUpper)
  hTitle = "BA - mu: pz"
  hLower = -4.0
  hUpper = 4.0
  hpzmuBA = hm.book(hTitle, hBins, hLower, hUpper)
  hTitle = "BA - muon decay: s"
  hLower = 300.0
  hUpper = 6000.0
  hmusBA = hm.book(hTitle, hBins, hLower, hUpper)
  hTitle = "BA - muon decay: x full"
  hLower = -10.0
  hUpper = 90.0
  hmuxFullBA = hm.book(hTitle, hBins, hLower, hUpper)
  hTitle = "BA - muon decay: x low"
  hLower = -1.0
  hUpper = 1.0
  hmuxLowBA = hm.book(hTitle, hBins, hLower, hUpper)
  hTitle = "BA - muon decay: x high"
  hLower = 80.0
  hUpper = 82.0
  hmuxHiBA = hm.book(hTitle, hBins, hLower, hUpper)
  hTitle = "BA - muon decay: y"
  hLower = -1.0
  hUpper = 1.0
  hmuyBA = hm.book(hTitle, hBins, hLower, hUpper)
  hTitle = "BA - muon decay: z"
  hLower = -50.0
  hUpper = 300.0
  hmuzBA = hm.book(hTitle, hBins, hLower, hUpper)

#   the plane plots - plane 1
  hTitle = "Muon decay Plane 1: s"
  hLower = 0.0
  hUpper = 500.0
  pl1MuDcyS = hm.book(hTitle, hBins, hLower, hUpper)
  hTitle = "Detector plane 1: numu x position"
  hLower = -200.0
  hUpper = 200.0
  pl1NumuX = hm.book(hTitle, hBins, hLower, hUpper)
  hTitle = "Detector plane 1: numu x small"
  hxLower = [-10.0,71.4]
  hxUpper = [10.0, 91.4]
  pl1NumuSm = hm.book(hTitle, hBins, hxLower[typPnt], hxUpper[typPnt])
  hTitle = "Detector plane 1: numu y position"
  hLower = -10.0
  hUpper = 10.0
  pl1NumuY = hm.book(hTitle, hBins, hLower, hUpper)
  hTitle = "Detector plane 1: Z position"
  hLower = -300.0
  hUpper = 300.0
  pl1NumuZ = hm.book(hTitle, hBins, hLower, hUpper)
  hTitle = "Detector plane 1: nue x position"
  hLower = -1000.0
  hUpper = 1000.0
  pl1Nue = hm.book(hTitle, hBins, hxLower[typPnt], hxUpper[typPnt])
  hTitle = "Detector plane 1: nue x small"
  hLower = -10.0
  hUpper = 10.0
  pl1NueSm = hm.book(hTitle, hBins, hLower, hUpper)
  hTitle = "Detector plane 1: nue y position"
  hLower = -10.0
  hUpper = 10.0
  pl1NueY = hm.book(hTitle, hBins, hLower, hUpper)

  hTitle = "Decay to plane 1: in Z for nue"
  hLower = -300.0
  hUpper = 300.0
  pl1DelZE = hm.book(hTitle, hBins, hLower, hUpper)
  hTitle = "Decay to plane 1: in Z for numu"
  hLower = -300.0
  hUpper = 300.0
  pl1DelZMu = hm.book(hTitle, hBins, hLower, hUpper)


#   the plane plots - plane 2

  hTitle = "Detector plane 2: numu x position"
  hLower = -200.0
  hUpper = 200.0
  pl2NumuX = hm.book(hTitle, hBins, hLower, hUpper)
  hTitle = "Detector plane 2: numu x small"
  hLower = -10.0
  hUpper = 10.0
  pl2NumuSm = hm.book(hTitle, hBins, hxLower[typPnt], hxUpper[typPnt])
  hTitle = "Detector plane 2: numu y position"
  hLower = -10.0
  hUpper = 10.0
  pl2NumuY = hm.book(hTitle, hBins, hLower, hUpper)
  hTitle = "Detector plane 2: Z position"
  hLower = -300.0
  hUpper = 300.0
  pl2NumuZ = hm.book(hTitle, hBins, hLower, hUpper)
  hTitle = "Detector plane 2: numu x small"
  hLower = -10.0
  hUpper = 10.0
  pl2Nue = hm.book(hTitle, hBins, hLower, hUpper)
  hTitle = "Detector plane 2: nue x small"
  hLower = -10.0
  hUpper = 10.0
  pl2NueSm = hm.book(hTitle, hBins, hxLower[typPnt], hxUpper[typPnt])
  hTitle = "Detector plane 2: nue y position"
  hLower = -10.0
  hUpper = 10.0
  pl2NueY = hm.book(hTitle, hBins, hLower, hUpper)

  hTitle = "Decay to plane 2: in Z for nue"
  hLower = -300.0
  hUpper = 300.0
  pl2DelZE = hm.book(hTitle, hBins, hLower, hUpper)
  hTitle = "Decay to plane 2: in Z for numu"
  hLower = -300.0
  hUpper = 300.0
  pl2DelZMu = hm.book(hTitle, hBins, hLower, hUpper)


  ##! Start:
  print("========  plane2: tests start  ========")

  ##! Test plane position
  planeTest = 1
  print()
  print("planeTest:", planeTest, " check constructor.")
  xPos = [0.0, 81.4]
  print(f"xPos is {xPos}")
  yPos = 0.0
  zPos1 = 230.0
  position1 = [xPos[typPnt], yPos, zPos1]
  d1 = plane.plane(position1)
  if (__DBG): print (f"d1 is {d1}")

  yPos = 0.0
  zPos2 = -50.0
  position2 = [xPos[typPnt], yPos, zPos2]
  d2 = plane.plane(position2)
  if (__DBG): print (f"d2 is {d2}")


  sVal = 140.0  
  xVal = 0.0
  yVal = 0.0
  zVal = sVal - 50.0
  xpVal = 0.0
  ypVal = 0.0
  tS = np.array([sVal, xVal, yVal, zVal, xpVal, ypVal])
  if (__DBG): print(f"tS is {tS}")
  if (__DBG): print(f"          s,   x,   y,   z,   xp,   yp")

  ps = 0
  rs = 0
  tArc = 0
  bArc = 0
  ringErr = 0
  dirENu1 = 0
  dirMuNu1 = 0
  negMuMom = 0
  dirENu2 = 0
  dirMuNu2 = 0

  noDcyLengthCut = 0

  xCompECt1 = 0
  xCompMuCt1 = 0
  xCompECtFl1 = 0
  xCompMuCtFl1 = 0
  xCompECt2 = 0
  xCompMuCt2 = 0
  xCompECtFl2 = 0
  xCompMuCtFl2 = 0

  
#  need to create a set up for creation of neutrino event instance
  nuSIMPATH = os.getenv('nuSIMPATH')
  filename  = os.path.join(nuSIMPATH, \
                         '11-Parameters/nuSTORM-PrdStrght-Params-v1.0.csv')
  pMuCentral= 6.0

  for count in range(20000):

    if (__DBG): 
      print ("\n======================================================")
      print(f"count is {count}")

    nuEI = nuEvtInst.NeutrinoEventInstance(pMuCentral,tS)
    if (__DBG): print(f"     nuEI {nuEI}")

    pE = nuEI.getnue4mmtm()[1]         # 3 vectors of the neutrinos
    pNuMu = nuEI.getnumu4mmtm()[1]       # checked these agree with the printout of nuEI
    pEl = nuEI.gete4mmtm()[1]
    if (__DBG): print (f"pEl is {pEl}")

    pMu=[0.0,0.0,0.0]
    pMu[0] = pE[0] + pNuMu[0] + pEl[0]
    pMu[1] = pE[1] + pNuMu[1] + pEl[1]
    pMu[2] = pE[2] + pNuMu[2] + pEl[2]
    if (__DBG): print (f"pMu is {pMu}")

    pEZ = pE[2]
    pNuMuZ = pNuMu[2]
    if (__DBG): 
      print(f"      pEZ is {pEZ}")
      print(f"      pNuMuZ is {pNuMuZ}")

    dcyPos = nuEI.getTraceSpaceCoord()  # checked z is same as the value in nuEI
    if (__DBG): print(f"      dcyPos  s:{dcyPos[0]}  x:{dcyPos[1]}  y:{dcyPos[2]}  z:{dcyPos[3]}  xp:{dcyPos[4]}  yp:{dcyPos[5]}")

    if (dcyPos[0] < 300): continue
    pl1MuDcyS.Fill(dcyPos[0])
    arcFlg = False
    noDcyLengthCut = noDcyLengthCut + 1
    if (dcyPos[3] >= 0.0 and dcyPos[3] <=180.0):
      if (dcyPos[1] < 20.0):
        if (__DBG): print (f"                      In straight z: {dcyPos[3]}")
        hmusPS.Fill(dcyPos[0])
        hmuxFullPS.Fill(dcyPos[1])
        hmuxLowPS.Fill(dcyPos[1])
        hmuxHiPS.Fill(dcyPos[1])
        hmuyPS.Fill(dcyPos[2])
        hmuzPS.Fill(dcyPos[3])

        hpxnumuPS.Fill(pNuMu[0])
        hpynumuPS.Fill(pNuMu[1])
        hpznumuPS.Fill(pNuMu[2])
        hpxnuePS.Fill(pE[0])
        hpynuePS.Fill(pE[1])
        hpznuePS.Fill(pE[2])
        hpxmuPS.Fill(pMu[0])
        hpymuPS.Fill(pMu[1])
        hpzmuPS.Fill(pMu[2])
        ps = ps + 1
        if (__DBG): print (f"typPnt  PS: {typPnt}")
        if typPnt == 0: 
          arcFlg = True
          if (__DBG): print (f"arcFlg  {arcFlg}")
      elif (dcyPos[1] >= 20.0):
        if (__DBG): print (f"                      In return straight z: {dcyPos[3]}")
        hmusRS.Fill(dcyPos[0])
        hmuxFullRS.Fill(dcyPos[1])
        hmuxLowRS.Fill(dcyPos[1])
        hmuxHiRS.Fill(dcyPos[1])
        hmuyRS.Fill(dcyPos[2])
        hmuzRS.Fill(dcyPos[3])

        hpxnumuRS.Fill(pNuMu[0])
        hpynumuRS.Fill(pNuMu[1])
        hpznumuRS.Fill(pNuMu[2])
        hpxnueRS.Fill(pE[0])
        hpynueRS.Fill(pE[1])
        hpznueRS.Fill(pE[2])
        hpxmuRS.Fill(pMu[0])
        hpymuRS.Fill(pMu[1])
        hpzmuRS.Fill(pMu[2])
        rs = rs + 1
        if (__DBG): print (f"typPnt  RS: {typPnt}")
        if typPnt == 1: 
          arcFlg = True
          if (__DBG): print (f"arcFlg  {arcFlg}")
    elif (dcyPos[3] < 0.0):
      if (__DBG): print (f"                      In top arc z: {dcyPos[3]}")
      tArc = tArc + 1
      hmusTA.Fill(dcyPos[0])
      hmuxFullTA.Fill(dcyPos[1])
      hmuxLowTA.Fill(dcyPos[1])
      hmuxHiTA.Fill(dcyPos[1])
      hmuyTA.Fill(dcyPos[2])
      hmuzTA.Fill(dcyPos[3])

      hpxnumuTA.Fill(pNuMu[0])
      hpynumuTA.Fill(pNuMu[1])
      hpznumuTA.Fill(pNuMu[2])
      hpxnueTA.Fill(pE[0])
      hpynueTA.Fill(pE[1])
      hpznueTA.Fill(pE[2])
      hpxmuTA.Fill(pMu[0])
      hpymuTA.Fill(pMu[1])
      hpzmuTA.Fill(pMu[2])
    elif (dcyPos[3] > 180.0):
      if (__DBG): print (f"                      In bottom arc z: {dcyPos[3]}")
      hmusBA.Fill(dcyPos[0])
      hmuxFullBA.Fill(dcyPos[1])
      hmuxLowBA.Fill(dcyPos[1])
      hmuxHiBA.Fill(dcyPos[1])
      hmuyBA.Fill(dcyPos[2])
      hmuzBA.Fill(dcyPos[3])

      hpxnumuBA.Fill(pNuMu[0])
      hpynumuBA.Fill(pNuMu[1])
      hpznumuBA.Fill(pNuMu[2])
      hpxnueBA.Fill(pE[0])
      hpynueBA.Fill(pE[1])
      hpznueBA.Fill(pE[2])
      hpxmuBA.Fill(pMu[0])
      hpymuBA.Fill(pMu[1])
      hpzmuBA.Fill(pMu[2])
      bArc = bArc + 1
    else:
      print ("should never get here")
      ringErr =ringErr + 1

    xDetPosE = 0.0
    yDetPosE = 0.0
    xDetPosMu = 0.0
    yDetPosMu = 0.0

    if arcFlg:
      deltaZE1 = zPos1 - dcyPos[3]
      deltaZMu1 = zPos1 - dcyPos[3]

      if (__DBG): 
        print (f"      deltaZE1 {deltaZE1}")
        print (f"      deltaZMu1 {deltaZMu1}")

      hitE,hitMu=d1.findHitPositionMuEvt(nuEI)

      if np.sign(deltaZE1) == np.sign(pEZ):
        if (__DBG): print (f"          e neutrino in the right direction plane 1    deltaZE1 {deltaZE1}     pEZ {pEZ}")
        dirENu1 = dirENu1 + 1
        xDetPosE = dcyPos[1] + deltaZE1*pE[0]/pE[2]
        yDetPosE = dcyPos[2] + deltaZE1*pE[1]/pE[2]
        pl1Nue.Fill(xDetPosE)
        pl1NueSm.Fill(xDetPosE)
        pl1NueY.Fill(yDetPosE)
        pl1DelZE.Fill(deltaZE1)
        if (__DBG): print (f"         xDetPosE {xDetPosE}    yDetPosE {yDetPosE}     zPos1 {zPos1}")

        if np.abs(hitE[0] - xDetPosE + xPos[typPnt]) < 0.0001:
          if (__DBG): 
            print("\n\nOK .... OK .... OK .... OK .... OK .... OK .... \n\n")
            print(f"hitE[0] {hitE[0]}     xDetPos  {xDetPosE}")
          xCompECt1 = xCompECt1 + 1
        else:
          xCompECtFl1 = xCompECtFl1 + 1
          if (__DBG): 
            print("\n\nFailed .... Failed .... Failed .... Failed .... \n\n")
            print(f"hitE[0] {hitE[0]}     xDetPosE  {xDetPosE}")


      if np.sign(deltaZMu1) == np.sign(pNuMuZ):
        if (__DBG): print (f"          mu neutrino in the right direction plane 1  deltaZMu1 {deltaZMu1}     pEZ {pNuMuZ}")
        dirMuNu1 = dirMuNu1 + 1
        xDetPosMu = dcyPos[1] + deltaZMu1*pNuMu[0]/pNuMu[2]
        yDetPosMu = dcyPos[2] + deltaZMu1*pNuMu[1]/pNuMu[2]
        pl1NumuX.Fill(xDetPosMu)
        pl1NumuSm.Fill(xDetPosMu)
        pl1NumuY.Fill(yDetPosMu)
        pl1NumuZ.Fill(zPos1)
        pl1DelZMu.Fill(deltaZMu1)
        if (__DBG): print (f"         xDetPosMu {xDetPosMu}    yDetPosMu {yDetPosMu}     zPos1 {zPos1}")

        if np.abs(hitMu[0] - xDetPosMu + xPos[typPnt]) < 0.0001:
          if (__DBG): 
            print("\n\nOK .... OK .... OK .... OK .... OK .... OK .... \n\n")
            print(f"hitMu[0] {hitMu[0]}     xDetPosMu  {xDetPosMu}")
          xCompMuCt1 = xCompMuCt1 + 1
        else:
          xCompMuCtFl1 = xCompMuCtFl1 + 1
          if (__DBG): 
            print("\n\nFailed .... Failed .... Failed .... Failed .... \n\n")
            print(f"hitMu[0] {hitMu[0]}     xDetPosMu  {xDetPosMu}")

    if arcFlg:
      deltaZE2 = zPos2 - dcyPos[3]
      deltaZMu2 = zPos2 - dcyPos[3]

      if (__DBG): 
        print (f"      deltaZE2 {deltaZE2}")
        print (f"      deltaZMu2 {deltaZMu2}")

      hitE,hitMu=d2.findHitPositionMuEvt(nuEI)

      if np.sign(deltaZE2) == np.sign(pEZ):
        if (__DBG): print (f"          e neutrino in the right direction plane 2  deltaZE2 {deltaZE2}     pEZ {pEZ}")
        dirENu2 = dirENu2 + 1
        xDetPosE = dcyPos[1] + deltaZE2*pE[0]/pE[2]
        yDetPosE = dcyPos[2] + deltaZE2*pE[1]/pE[2]
        pl2Nue.Fill(xDetPosE)
        pl2NueSm.Fill(xDetPosE)
        pl2NueY.Fill(yDetPosE)
        pl2NumuZ.Fill(zPos2)
        pl2DelZE.Fill(deltaZE2)
        if (__DBG): print (f"         xDetPosE {xDetPosE}    yDetPosE {yDetPosE}     zPos {zPos2}")

        if np.abs(hitE[0] - xDetPosE + xPos[typPnt]) < 0.0001:
          if (__DBG): 
            print("\n\nOK .... OK .... OK .... OK .... OK .... OK .... \n\n")
            print(f"hitE[0] {hitE[0]}     xDetPos  {xDetPosE}")
          xCompECt2 = xCompECt2 + 1
        else:
          xCompECtFl2 = xCompECtFl2 + 1
          if (__DBG): 
            print("\n\nFailed .... Failed .... Failed .... Failed .... \n\n")
            print(f"hitE[0] {hitE[0]}     xDetPosE  {xDetPosE}")


      if np.sign(deltaZMu2) == np.sign(pNuMuZ):
        if (__DBG): print (f"          mu neutrino in the right direction plane 2  deltaZMu2 {deltaZMu2}     pNuMuZ {pNuMuZ}")
        dirMuNu2 = dirMuNu2 + 1
        xDetPosMu = dcyPos[1] + deltaZMu2*pNuMu[0]/pNuMu[2]
        yDetPosMu = dcyPos[2] + deltaZMu2*pNuMu[1]/pNuMu[2]
        pl2NumuX.Fill(xDetPosMu)
        pl2NumuSm.Fill(xDetPosMu)
        pl2NumuY.Fill(yDetPosMu)
        pl2DelZMu.Fill(deltaZMu2)
        if (__DBG): print (f"         xDetPosMu {xDetPosMu}    yDetPosMu {yDetPosMu}     zPos2 {zPos2}")

        if np.abs(hitMu[0] - xDetPosMu + xPos[typPnt]) < 0.0001:
          if (__DBG): 
            print("\n\nOK .... OK .... OK .... OK .... OK .... OK .... \n\n")
            print(f"hitMu[0] {hitMu[0]}     xDetPosMu  {xDetPosMu}")
          xCompMuCt2 = xCompMuCt2 + 1
        else:
          xCompMuCtFl2 = xCompMuCtFl2 + 1
          if (__DBG): 
            print("\n\nFailed .... Failed .... Failed .... Failed .... \n\n")
            print(f"hitMu[0] {hitMu[0]}     xDetPosMu  {xDetPosMu}")




      if pMu[0] < -0.25: 
        negMuMom = negMuMom + 1


  print(f"\n\n       production straight decays {ps}")
  print(f"       return straight decays {rs}")
  print(f"       top arc decays {tArc}")
  print(f"       bottom arc decays {bArc}")
  print(f"       ring errors {ringErr}")
  print(f"       noDcyLengthCut {noDcyLengthCut}")

  print(f"       dirENu1 {dirENu1}")
  print(f"       dirMuNu1 {dirMuNu1}")
  print(f"       dirENu2 {dirENu2}")
  print(f"       dirMuNu2 {dirMuNu2}")
  print(f"       negMuMom {negMuMom}")

  print(f"       xCompECt1  {xCompECt1}      xCompECtFl1  {xCompECtFl1}")
  print(f"       xCompMuCt1  {xCompMuCt1}    xCompMuCtFl1  {xCompMuCtFl1}")
  print(f"       xCompECt2  {xCompECt2}      xCompECtFl2  {xCompECtFl2}")
  print(f"       xCompMuCt2  {xCompMuCt2}    xCompMuCtFl2  {xCompMuCtFl2}")

  #hmusPS.Fit('gaus')
  #hmusRS.Fit('gaus')
  #hmusTA.Fit('gaus')
  #musBA.Fit('gaus')

  print(f"shrtRun is {__shrtRun}")
  if __shrtRun == False: hm.histdo(histDir)

  passed = 0
  failed = 0

  print(f"passed is {passed}")
  print(f"failed is {failed}")
  print()
  print("========  plane2: tests complete  ========")
  print ("testFails is ", testFails)

  if __shrtRun == False: hm.texCreate(texDir)

  if (testFails == 0):
    sys.exit(0)
  else:
    sys.exit(1)
