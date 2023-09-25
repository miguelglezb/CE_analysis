#!/bin/bash

chk_pip=`which pip | wc -l`
chk_pip3=`which pip3 | wc -l` 



if [ $chk_pip != 0 ];
then 
    echo 'pip is installed' 
    sudo pip install -r requirements.txt
fi

if [ $chk_pip3 != 0 ];
then 
    echo 'pip3 is installed' 
    sudo pip3 install -r requirements.txt
fi

if [ $chk_pip3 = 0 ] && [ $chk_pip = 0 ]; 
then
    echo 'Neither pip version is installed, pip3 will be installed now.'
    sudo apt install python3-pip
    sudo pip install -r requirements.txt
fi
