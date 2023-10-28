#!/usr/bin/python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import sarracen as sar
import sys
import utils.dataread as dr
import seaborn as sns
import matplotlib.ticker as ticker
from utils.wdata import write_hist2D_data
from separation import sep_t
from utils.rdumpfiles import read_dumpfiles
from utils.units import constants
from utils.pformat import save_figure, plot_format
from energies import potential_parts, kinetic_parts
from tqdm import tqdm  
from cli_args_system import Args
from matplotlib.ticker import ScalarFormatter

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
    sdf, sdf_sink = sar.read_phantom(dumpfile_list[0])
    weight = sdf.params['mass']
    for npart,i in zip(dict_ubn,tqdm(range(nloops2))):
        tR = dict_ubn[npart]
        time = np.append(time, tR[0])
        R = np.append(R, tR[1])   
    return time, np.log10(R), weight


if __name__ == "__main__":
    yr = constants.yr
    erg = constants.ener
    args = Args(convert_numbers=True)

    #List of flags
    evy_file = args.flag_str('evy','evy_file')
    path_save = args.flag_str('s','save')

    #Define path of dumpfiles and for plot/data saving
    path_dumpfiles = './data/CE_example/'   
    if len(sys.argv) > 1:
        if sys.argv[1][0] != '-':
            path_dumpfiles = sys.argv[1] + '/'
    if path_save == None:
        path_save = path_dumpfiles

    #Generate list of dumpfiles 
    dump_list = read_dumpfiles(path=path_dumpfiles,evy_files=evy_file)
    time_newly_unb, logR_newly_unb, weight = unbound_mech_kipp(dump_list)

    #Generate data for histogram 
    write_hist2D_data(time_newly_unb, logR_newly_unb, 'time', 'logR', weight,pathfile=path_save)
    ph_data = dr.phantom_evdata(path_dumpfiles + '/separation_vs_time.ev',pheaders=False)
    
    #Plot declaration  
    ax = plt.gca()
    ax.plot(ph_data['time']*yr, np.log10(ph_data['sep. 1'])) 
   
    #Histogram format   
    nbins = min([int(len(dump_list)/1.05),500])
    kipp_unb = sns.histplot(x=time_newly_unb, y=logR_newly_unb, ax=ax,color='r', weights=weight, 
                            bins=nbins, cbar=True, cbar_kws=dict(shrink=.90))

    #Colorbar format
    formatter = ScalarFormatter(useMathText=True)
    formatter.set_powerlimits((-7, -2)) 
    kipp_unb.collections[0].colorbar.ax.yaxis.set_major_formatter(formatter)
    kipp_unb.collections[0].colorbar.set_label('Mass [M$_{\odot}$]', fontsize=18)

    #Labels' format
    plot_format('time [yr]', 'R$_{\odot}$', leg=False)
    
    plt.show()