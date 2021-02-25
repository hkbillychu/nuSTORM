#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test script for "Simulation" class ... initialisation and get methods
==================================

  Simulation.py -- set "relative" path to code

"""

import Simulation as Simu

##! Start:
print("========  Simulation: start  ========")
print()

Smltn = Simu.Simulation(50, 5., '11-Parameters/nuSTORM-PrdStrght-Params-v1.0.csv', 'nuSTORM.root')

print()
print(".... Execute simulation")

Smltn.RunSim()

##! Complete:
print()
print("========  Simulation: complete  ========")
