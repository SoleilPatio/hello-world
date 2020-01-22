#!/bin/bash

#----------------------
for i in {a..c}; do echo $(printf "%s %d" "$i" "''$i"); done

#----------------------
VAR=abcdef
echo ${VAR:${#VAR}-3:${#VAR}-1}

#----------------------
A=1
B=2
echo $((A+B))

#----------------------
RANDOM=`date +%s`
echo $RANDOM
echo $RANDOM

#----------------------
function_test()
{
    echo "0:"$0
    echo "1:"$1
    echo "2:"$2
    echo "@:"$@
    echo "#:"$#
}

function_test arg1 arg2