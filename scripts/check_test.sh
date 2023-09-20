#!/bin/bash

sep_file=figs/separation.pdf
mech_ener_file=figs/mech_ener.pdf

if [ -f "$sep_file" ]; then
    echo '\n Orbital separation test passed! \n'
else
    echo '\n Orbital separation test failed! \n'
fi

if [ -f "$mech_ener_file" ]; then
    echo '\n Mechanical energy test passed! \n'
else
    echo '\n Mechanical energy test failed! \n'
fi

if [ -f "$sep_file" ] && [ -f "$mech_ener_file" ]; then
    echo '\n Test passed!!!' 
fi

