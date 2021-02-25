#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Class: ntupleMake:
==================

Outputs nuStorm monte-carlo production data as a root ntuple

Version 2.5 									25/02/2021
Author: Paul Kyberd
Modify treeFill() method to output one event at a time

Version 2.4										24/02/2021
Author: Paul Kyberd
Include the time of the decay as part of the decay information.
This is the time in picoseconds since the start of the machine 
spill.


Version 2.3										17/02/2021
Author: Paul Kyberd
Make the run number a parameter passed in as part of __init__

Version 2.2										16/02/2021
Author: Paul Kyberd
Add run number to the data structure and include it in a new
branch of the tree, which is only written once at the start
of the run

Version 2.1										08/02/2021
Author: Paul Kyberd
Change the name of the root event object to reflect the version
of the format of the data output

Version 2.0										08/02/2021
Rewrite output as a TTree

Version 1.1										05/02/2021
Modify the variables output in the root file

Version 1.0										01/02/2021
Initial version

'''

# Generic Python imports
import sys, os

import array
# numpy
import numpy as np

# pyRoot imports
import ROOT
from ROOT import TFile, TNtuple, gROOT, TROOT, TTree, AddressOf, addressof

# nuStorm imports
import MuonConst as MuonConst
import NeutrinoEventInstance as nuEvtInst

#  Need a structure so 
gROOT.ProcessLine(
"struct information {\
   Float_t          runNumber;\
   Float_t          Version;\
   Float_t			PWidth;\
   Float_t          PHeight;\
   Float_t          PZ;\
   Float_t			DBWidth;\
   Float_t          DBHeight;\
   Float_t          DBDepth;\
   Float_t          DBZ;\
   Char_t           emmitanceUnits[2];\
};" );
gROOT.ProcessLine(
"struct event_t {\
   Float_t         Emu;\
   Float_t         pMuX;\
   Float_t         pMuY;\
   Float_t         pMuZ;\
   Float_t         s;\
   Float_t         x;\
   Float_t         y;\
   Float_t         z;\
   Float_t         xp;\
   Float_t         yp;\
   Float_t         t;\
   Float_t         Ee;\
   Float_t         peX;\
   Float_t         peY;\
   Float_t         peZ;\
   Float_t         Enumu;\
   Float_t         pnumuX;\
   Float_t         pnumuY;\
   Float_t         pnumuZ;\
   Float_t         Enue;\
   Float_t         pnueX;\
   Float_t         pnueY;\
   Float_t         pnueZ;\
};" );

muCnst = MuonConst.MuonConst()

class ntupleMake:
	Version = 2.5
	__Validated__ = False
	outputFilename="" 
	__muMass = muCnst.mass()/1000.

# built-in methods
	def __init__(self, runNum, outputFilename="nuStorm.root"):

		self.outputFilename = outputFilename
		self.outfile = TFile( self.outputFilename, 'RECREATE', 'ROOT file with an NTuple' )
# first a TTree with the run information - written once
		self.runInfo = ROOT.information()
		self.infoTree = TTree('runInfo', 'run information')
		self.infoTree.Branch( 'information', self.runInfo, 'runNumber/F:Version:FluxPlaneW:FluxPlaneH:PZ:DetectW:DetecH:DetecD:DetecZ:Emit')
#		self.infoTree.Branch( 'Flux Plane', AddressOf( self.runInfo, 'PWidth'), 'Width/F:Height:Z')
#		self.infoTree.Branch( 'Detector Box', AddressOf( self.runInfo, 'DBWidth'), 'Width/F:Height:Depth:Z')

# Parameters for the run
		self.runInfo.runNumber = runNum
		self.runInfo.Version = self.Version

# Parameters for the flux plane
		self.runInfo.PWidth = 10.0
		self.runInfo.PHeight = 10.0
		self.runInfo.PZ = 50.0
# Parameters for the detector box
		self.runInfo.DBWidth = 20.0
		self.runInfo.DBHeight = 20.0
		self.runInfo.DBDepth = 20.0
		self.runInfo.DBZ = 50.0
		self.emittanceUnits = 'mm'

		self.infoTree.Fill()
		self.infoTree.Write()

# a TTree for the data from every event
		self.event = ROOT.event_t()
		self.evTree = TTree('beam', 'nuStorm Event')
		self.evTree.Branch( 'muon', self.event, 'E/F:pX:pY:pZ' )
		self.evTree.Branch( 'Decay', addressof( self.event, 's'), 's/F:x:y:z:xp:yp:t')
		self.evTree.Branch( 'Electron', addressof( self.event, 'Ee'), 'E/F:pX:pY:pZ')
		self.evTree.Branch( 'NuMu', addressof( self.event, 'Enumu'), 'E/F:pX:pY:pZ')
		self.evTree.Branch( 'Nue', addressof( self.event, 'Enue'), 'E/F:pX:pY:pZ')


	def __repr__(self):
		return "make an TTree"

	def __str__(self):
		return "ntuple Maker: outputFilename = %s" \
		         % \
               (self.outputFilename)

	def treeFill(self, nuEvt):

# tracespace coordinates of the decay point
		self.event.s = nuEvt.getTraceSpaceCoord()[0]
		self.event.x = nuEvt.getTraceSpaceCoord()[1]
		self.event.y = nuEvt.getTraceSpaceCoord()[2]
		self.event.z = nuEvt.getTraceSpaceCoord()[3]
		self.event.xp = nuEvt.getTraceSpaceCoord()[4]
		self.event.yp = nuEvt.getTraceSpaceCoord()[5]
		self.event.t = 0.0;
# get the 4 vector of the muon, currently along the z axis
		self.event.pMuX = 0.0
		self.event.pMuY = 0.0
		self.event.pMuZ = nuEvt.getpmu()
		self.event.Emu  = np.sqrt(self.event.pMuZ**2 + self.__muMass**2)
# get the 4 vector of the electron
		self.event.Ee  = nuEvt.gete4mmtm()[0]
		self.event.peX = nuEvt.gete4mmtm()[1][0]
		self.event.peY = nuEvt.gete4mmtm()[1][1]
		self.event.peZ = nuEvt.gete4mmtm()[1][2]
# get the 4 vector of the muon neutrino
		self.event.Enumu  = nuEvt.getnumu4mmtm()[0]
		self.event.pnumuX = nuEvt.getnumu4mmtm()[1][0]
		self.event.pnumuY = nuEvt.getnumu4mmtm()[1][1]
		self.event.pnumuZ = nuEvt.getnumu4mmtm()[1][2]
# get the 4 vector of the muon neutrino
		self.event.Enue  = nuEvt.getnue4mmtm()[0]
		self.event.pnueX = nuEvt.getnue4mmtm()[1][0]
		self.event.pnueY = nuEvt.getnue4mmtm()[1][1]
		self.event.pnueZ = nuEvt.getnue4mmtm()[1][2]

		self.evTree.Fill()

	def output(self):
#	Write out the data
		self.evTree.Write()
		return


	def closeFile(self):
		self.evTree.Print()
		self.evTree.Write()
		return

	def initNtuple(self, labels):
		self.ntuple  = TNtuple( 'ntuple', ' nuStorm source', ':'.join( labels ) )
		if self.__Validated__: print ("ntuple is ", self.ntuple)
		return


# Test to run if file is invoked as the main programme
if __name__ == "__main__" : 


	print(" running as main - run tests")

##! Generate events:
	nuEI = []
	for i in range(20):
		nuEI.append(nuEvtInst.NeutrinoEventInstance(5.))

	nt = ntupleMake("test.root")
	nt.treeFill(nuEI)	

	print(" tests finished - check file test.root")
