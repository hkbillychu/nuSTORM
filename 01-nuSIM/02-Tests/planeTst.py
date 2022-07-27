#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test script for updated "plane2" class ...
==========================================

  plane2.py -- set "relative" path to code

"""

import plane2 as plane
import NeutrinoEventInstance as nuEvtInst
import traceSpace as trSp
import histoManager
import numpy as np
import sys, os
from statistics import mean


class planeTst():

  __DBG = False

  histDir = "/Users/paulkyberd/work/nuStudy"
  texDir = "/Users/paulkyberd/work/nuStudy/testing.tex"

  hm = histoManager.histoManager()

  testFails = 0

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

#   the plane plots
  hTitle = "Detector plane: numu x position"
  hLower = -1000.0
  hUpper = 1000.0
  plNumu = hm.book(hTitle, hBins, hLower, hUpper)
  hTitle = "Detector plane: numu x small"
#  hLower = -10.0
#  hUpper = 10.0
  hLower = 71.0
  hUpper = 91.0
  plNumuSm = hm.book(hTitle, hBins, hLower, hUpper)
  hTitle = "Detector plane: numu y position"
  hLower = -10.0
  hUpper = 10.0
  plNumuY = hm.book(hTitle, hBins, hLower, hUpper)
  hTitle = "Detector plane: nue x position"
  hLower = -1000.0
  hUpper = 1000.0
  plNue = hm.book(hTitle, hBins, hLower, hUpper)
  hTitle = "Detector plane: nue x small"
  hLower = 71.0
  hUpper = 91.0
  plNueSm = hm.book(hTitle, hBins, hLower, hUpper)
  hTitle = "Detector plane: nue y position"
  hLower = -10.0
  hUpper = 10.0
  plNueY = hm.book(hTitle, hBins, hLower, hUpper)

  hTitle = "Decay to plane: in Z for nue"
  hLower = -300.0
  hUpper = 300.0
  plDelZE = hm.book(hTitle, hBins, hLower, hUpper)
  hTitle = "Decay to plane: in Z for numu"
  hLower = -300.0
  hUpper = 300.0
  plDelZMu = hm.book(hTitle, hBins, hLower, hUpper)





  ##! Start:
  print("========  plane2: tests start  ========")

  ##! Test plane position
  planeTest = 1
  print()
  print("planeTest:", planeTest, " check constructor.")
  zPos = -50.0
  xPos = 81.4
  yPos = 0.0
  position = [xPos, yPos, zPos]

  d1 = plane.plane(position)
  if (__DBG): print (f"d1 is {d1}")

  sVal = 100.0
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
  dirENu = 0
  dirMuNu = 0
  negMuMom = 0

  xCompECt = 0
  xCompMuCt = 0
  xCompECtFl = 0
  xCompMuCtFl = 0

  for count in range(20000):

    if (__DBG): 
      print ("\n======================================================")
      print(f"count is {count}")
#  need to create a neutrino event instance
    nuSIMPATH = os.getenv('nuSIMPATH')
    filename  = os.path.join(nuSIMPATH, \
                         '11-Parameters/nuSTORM-PrdStrght-Params-v1.0.csv')
    pMuCentral= 3.0
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


    arcFlg = False
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
        arcFlg = True
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
      deltaZE = zPos - dcyPos[3]
      deltaZMu = zPos - dcyPos[3]

      if (__DBG): 
        print (f"      deltaZE {deltaZE}")
        print (f"      deltaZMu {deltaZMu}")

      hitE,hitMu=d1.findHitPositionMuEvt(nuEI)

      if np.sign(deltaZE) == np.sign(pEZ):
        if (__DBG): print ("          e neutrino in the right direction")
        dirENu = dirENu + 1
        xDetPosE = dcyPos[1] + deltaZE*pE[0]/pE[2]
        yDetPosE = dcyPos[2] + deltaZE*pE[1]/pE[2]
        plNue.Fill(xDetPosE)
        plNueSm.Fill(xDetPosE)
        plNueY.Fill(yDetPosE)
        plDelZE.Fill(deltaZE)
        if (__DBG): print (f"         xDetPosE {xDetPosE}    yDetPosE {yDetPosE}     zPos {zPos}")

        if np.abs(hitE[0] - xDetPosE + xPos) < 0.0001:
          if (__DBG): 
            print("\n\nOK .... OK .... OK .... OK .... OK .... OK .... \n\n")
            print(f"hitE[0] {hitE[0]}     xDetPos  {xDetPosE}")
          xCompECt = xCompECt + 1
        else:
          xCompECtFl = xCompECtFl + 1
          if (__DBG): 
            print("\n\nFailed .... Failed .... Failed .... Failed .... \n\n")
            print(f"hitE[0] {hitE[0]}     xDetPosE  {xDetPosE}")


      if np.sign(deltaZMu) == np.sign(pNuMuZ):
        if (__DBG): print ("          mu neutrino in the right direction")
        dirMuNu = dirMuNu + 1
        xDetPosMu = dcyPos[1] + deltaZE*pNuMu[0]/pNuMu[2]
        yDetPosMu = dcyPos[2] + deltaZE*pNuMu[1]/pNuMu[2]
        plNumu.Fill(xDetPosMu)
        plNumuSm.Fill(xDetPosMu)
        plNumuY.Fill(yDetPosMu)
        plDelZMu.Fill(deltaZMu)
        if (__DBG): print (f"         xDetPosMu {xDetPosMu}    yDetPosMu {yDetPosMu}     zPos {zPos}")

        if np.abs(hitMu[0] - xDetPosMu + xPos) < 0.0001:
          if (__DBG): 
            print("\n\nOK .... OK .... OK .... OK .... OK .... OK .... \n\n")
            print(f"hitMu[0] {hitMu[0]}     xDetPosMu  {xDetPosMu}")
          xCompMuCt = xCompMuCt + 1
        else:
          xCompMuCtFl = xCompMuCtFl + 1
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

  print(f"       dirENu {dirENu}")
  print(f"       dirMuNu {dirMuNu}")
  print(f"       negMuMom {negMuMom}")

  print(f"       xCompECt  {xCompECt}      xCompECtFl  {xCompECtFl}")
  print(f"       xCompMuCt  {xCompMuCt}    xCompMuCtFl  {xCompMuCtFl}")

  #hmusPS.Fit('gaus')
  #hmusRS.Fit('gaus')
  #hmusTA.Fit('gaus')
  #musBA.Fit('gaus')


  hm.histdo(histDir)

  passed = 0
  failed = 0

  print(f"passed is {passed}")
  print(f"failed is {failed}")
  print()
  print("========  plane2: tests complete  ========")
  print ("testFails is ", testFails)

  hm.texCreate(texDir)

  if (testFails == 0):
    sys.exit(0)
  else:
    sys.exit(1)
