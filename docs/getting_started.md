# Getting started

### [Home](./index.md)

Since this code is written in Python, the usage is almost straightforward. For now, it is only fully functional in linux (debian) OS. We plan to add mac SO in the near future.

## Pre-requisites

This code is written in Python 3, therefore it is required to have it installed. Additionally, some latex font packages are required to use the code. The complete disk size of these packages is ~200 MB. 

## Download

This code can be downloaded from the CE_analysis [repository](https://github.com/miguelglezb/CE_analysis), or simply by typing in the terminal:

`git clone https://github.com/miguelglezb/CE_analysis.git`

or, if the user has a SSH key in their github account:

`git clone git@github.com:miguelglezb/CE_analysis.git`

## Install

Installation of additional packages and modules used by CE_analysis is done by typing in the code directory:

 `sudo make install`

This will install the following Python modules:

-``matplotlib``  

-``numba``

-``pandas``

-``scipy``

-``seaborn``

-``sarracen``
 
It will also install the latex font (and extra) packages:

-``exlive-extra-utils`` 

-``cm-super`` 

-``texlive-latex-extra`` 

-``dvipng``

## Test

If installation of all packages is succesful, a simple test can be run. This test will download a common envelope model **(6GB disk space)** and will generate two plots from this data. The first plot is the orbital separation and the second is mechanical energy of the system as function of time. These two plots will be save in the ``figs`` directory (if it does not exist in the CE_analysis directory, it will create it).

To execute this test, type:

`make test`

in CE_analysis directory. If test is done successfully, a output message will indicate it at the end of the run.




