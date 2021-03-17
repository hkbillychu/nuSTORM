#!/bin/bash

stm=$(PWD)
#echo $stm
add="/01-Code"
#echo $add
dir="$stm$add"
#echo $dir

echo "Set nuSIM path:"
nuSIMPATH="$dir"
echo "    " $nuSIMPATH
export nuSIMPATH

echo "Set PYTHON path:"
PYTHONPATH="${PYTHONPATH}:$dir"
echo "    " $PYTHONPATH
export PYTHONPATH
