#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test script for "MuonConst" class
=================================

  Assumes that Code directory (01-Code) is in PYTHONPATH.

Version history:
----------------
 1.1: 09Feb20: KL: Prepared for "release"
 1.0: 31Dec20: First implementation

"""

import MuonConst as mc

##! Start:
print("========  MuonConst: tests start  ========")

##! Test singleton class feature:
MuonConstTest = 1
print()
print("MuonConstTest:", MuonConstTest, " check if class is a singleton.")
muCnst  = mc.MuonConst()
muCnst1 = mc.MuonConst()
print("    muCnst singleton test:", id(muCnst), id(muCnst1), id(muCnst)-id(muCnst1))
if muCnst != muCnst1:
    raise Exception("MuonConst is not a singleton class!")

##! Check built-in methods:
MuonConstTest = 2
print()
print("MuonConstTest:", MuonConstTest, " check built-in methods.")
print("    __repr__:")
print(muCnst)

##! Check get methods:
MuonConstTest = 3
print()
print("MuonConstTest:", MuonConstTest, " check get methods.")
print("----> print() method; tests all get methods")
muCnst.print()

##! Complete:
print()
print("========  MuonConst: tests complete  ========")
