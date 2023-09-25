#!/bin/bash

chk_pip=`which pip | wc -l`
chk_pip3=`which pip3 | wc -l` 



if [ $chk_pip != 0 ];
then 
    echo 'pip is installed' 
    #pip install -r requirements.txt
fi

if [ $chk_pip3 != 0 ];
then 
    echo 'pip3 is installed' 
    #pip3 install -r requirements.txt
fi

if [ $chk_pip3 = 0 ] && [ $chk_pip = 0 ]; 
then
    echo 'Neither pip version is installed, pip3 will be installed now.'
    #sudo apt install pip3
fi
