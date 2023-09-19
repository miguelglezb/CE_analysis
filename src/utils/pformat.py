#!/usr/bin/python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from matplotlib import rc
from matplotlib import rcParams
import os

scale = 1.5
rc('font',**{'family':'Times New Roman'})
rc('text', usetex=True)
rcParams["figure.figsize"] = [6.4*scale, 4.8*scale]


def plot_format(xlab,ylab,leg=True,grd=True,xlsize=20,ylsize=20,lgdsize=20,tksize=20):
    '''
    Adds personalised format to simple plots  

    Parameters 
    ----------
    xlab : str
        x-label for plot, if started and ended by $ it will print LaTeX math form
        (same with y-label)

    ylab : str
        x-label for plot

    leg : bool, optional
        If True, enables legend in plot

    grd : bool, optional
        If True, enables legend in plot

    xlsize: int
        Fontsize of x-label. Default is 20

    ylsize: int
        Fontsize of y-label. Default is 20

    lgdsize: int
        Fontsize of legend. Default is 20         
    '''
    plt.xlabel(xlab, fontsize=xlsize)
    plt.ylabel(ylab, fontsize=ylsize)
    plt.tick_params(labelsize=tksize)

    if grd==True:
        plt.grid()
    if leg==True:
        plt.legend(fontsize=lgdsize)

def save_figure(name='./',t=0.985,b=0.125,l=0.25,r=0.992,h=0.2,w=0.2):
    path = name
    plt.subplots_adjust(top=0.985, bottom=0.125, left=0.25, right=0.992, hspace=0.2, wspace=0.2)
    plt.savefig(path)
    plt.close()
    os.system('pdfcrop ' + path + ' ' + path)