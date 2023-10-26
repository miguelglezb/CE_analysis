#!/usr/bin/python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import sarracen as sar
import sys
from separation import sep_t
from utils.rdumpfiles import read_dumpfiles
from utils.units import constants
from utils.pformat import save_figure, plot_format
from energies import potential_parts, kinetic_parts
import utils.dataread as dr
import seaborn as sns
from tqdm import tqdm  
from cli_args_system import Args

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
    args = Args(convert_numbers=True)
    evy_file = args.flag_str('evy','evy_file')
    path_save = args.flag_str('s','save')
    path_dumpfiles = './data/CE_example/'   

    if len(sys.argv) > 2:
        if sys.argv[1][0] != '-':
            path_dumpfiles = sys.argv[1] + '/'
        if path_save == None:
            path_save = path_dumpfiles
    dump_list = read_dumpfiles(path=path_dumpfiles,evy_files=evy_file)

    time_newly_unb, logR_newly_unb = unbound_mech_kipp(dump_list)
    ph_data = dr.phantom_evdata(path_dumpfiles + '/separation_vs_time.ev',pheaders=False)
    
    fig, ax = plt.subplots()
    ax.plot(ph_data['time']*yr, np.log10(ph_data['sep. 1'])) 
    nbins = min([int(len(dump_list)/2),500])
    print(nbins)
    sns.histplot(x=time_newly_unb,y=logR_newly_unb, ax=ax,color='r',bins=nbins)
    ax.grid()
    plot_format('time [yr]', 'R$_{\odot}$', leg=False)
    save_figure(path_dumpfiles + '/newly_unb.pdf')
