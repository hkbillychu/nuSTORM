#!/bin/bash

# set up the PYTHONPAATH must be sourced before running nuSIM

stm=$PWD
#echo $stm

dir="$stm"
echo "Set nuSIM path:"
nuSIMPATH="$dir"
echo "    " $nuSIMPATH
export nuSIMPATH

add="/01-Code"
add2="/12-examples"
add3="/04-Studies"
add4="/11-Parameters"

#echo $add
dir="$stm$add"
dir2="$stm$add2"
dir3="$stm$add3"
dir4="$stm$add4"
#echo $dir
echo "Set PYTHON path:"
PYTHONPATH="${PYTHONPATH}:$dir:$dir2:$dir3:$dir4"
echo "    " $PYTHONPATH
export PYTHONPATH
