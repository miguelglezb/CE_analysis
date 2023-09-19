#!/bin/bash

nfiles_CE_dir=`ls data/CE_example/binary_* | wc -l`
CE_dir=data/CE_example

echo "\n Checking in local for simulation test... \n "

if [ $nfiles_CE_dir != 451 ]; 
then
    if [ -d "$CE_dir" ]; then
        echo "\n $CE_dir exists but does not have right number of dumpfiles. \n Downloading simulation sample..."
        rm -r data/CE_example
    fi
    wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=11O2F2MRESjQEGmkvlcxufhOc3WIHOzDk' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=11O2F2MRESjQEGmkvlcxufhOc3WIHOzDk" -O data/CE_example.zip && rm -rf /tmp/cookies.txt
    unzip data/CE_example.zip -d data/
    rm data/CE_example.zip
else
    echo "\n $CE_dir seems to have the right dumpfiles\n"
fi