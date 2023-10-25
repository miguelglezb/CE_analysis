#!/usr/bin/python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import sarracen as sar
import sys
from matplotlib import rc
from matplotlib import rcParams
from separation import sep_t
from utils.rdumpfiles import read_dumpfiles
from utils.vector_math import recentre_from_sink
from utils.units import constants
from utils.pformat import save_figure, plot_format
import utils.save_test_figs as stf
from energies import potential_parts, kinetic_parts
import dataread as dr
import seaborn as sns
from tqdm import tqdm  

def unbound_mech_kipp(dumpfile_list):
    time, R = np.array([]), np.array([])
    dict_ubn = {}
    nloops1 = len(dumpfile_list)
    for dump,i in zip(reversed(dumpfile_list),tqdm(range(nloops1))):
        t, r1, pot_energy_parts = potential_parts(dump,rtrack=True)
        t, kin_energy_parts = kinetic_parts(dump)
        nb = np.where(pot_energy_parts + kin_energy_parts > 0)[0]
        for npart in nb:
            dict_ubn.update({str(npart):[t*yr,r1[npart]]})
    nloops2 = len(dict_ubn.keys())    
    for npart,i in zip(dict_ubn.keys(),tqdm(range(nloops2))):
    #for npart in dict_ubn.keys():
        tR = dict_ubn[npart]
        time = np.append(time, tR[0])
        R = np.append(R, tR[1])   
    return time, np.log10(R)

if __name__ == "__main__":
    yr = constants.yr
    erg = constants.ener
    path_dumpfiles, path_save = './data/CE_example/', './'    
    if len(sys.argv) > 1:
        path_dumpfiles = sys.argv[1] + '/'
        path_save = sys.argv[-1] + '/'
    dump_list = read_dumpfiles(path=path_dumpfiles)
    time_newly_unb, logR_newly_unb = unbound_mech_kipp(dump_list)
    ph_data = dr.phantom_evdata(path_dumpfiles + '/separation_vs_time.ev',pheaders=False)
    fig, ax = plt.subplots()
    ax.plot(ph_data['time']*yr, np.log10(ph_data['sep. 1'])) 
    sns.histplot(x=time_newly_unb,y=logR_newly_unb, ax=ax,color='r')
    #H, yedges, xedges = np.histogram2d(logR_newly_unb,time_newly_unb,bins=200)
    #plt.pcolormesh(xedges, yedges, H+1, cmap='Reds')
    plt.show()

