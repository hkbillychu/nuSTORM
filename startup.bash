#!/bin/bash

stm=$(PWD)
echo $stm
add="/01-Code"
echo $add
dir="$stm$add"
echo $dir

PYTHONPATH="${PYTHONPATH}:$dir"
echo $PYTHONPATH
export PYTHONPATH
