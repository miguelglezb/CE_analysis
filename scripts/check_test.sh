#!/bin/bash

sep_file=figs/separation.pdf
mech_ener_file=figs/mech_ener.pdf

if [ -f "$sep_file" ]; then
    echo '\n Orbital separation plot found! \n'
else
    echo '\n ERROR: Orbital separation plot not found! \n'
fi

if [ -f "$mech_ener_file" ]; then
    echo '\n Mechanical energy plot found! \n'
else
    echo '\n ERROR: Mechanical energy plot not found! \n'
fi

if [ -f "$sep_file" ] && [ -f "$mech_ener_file" ]; then
    echo '\n TEST PASSED!!!\n' 
fi

cat extras/CE_logo.txt
