#!/usr/bin/python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc
from matplotlib import rcParams
import sarracen as sar
import sys
from utils.rdumpfiles import read_dumpfiles
from utils.units import constants
from utils.pformat import save_figure, plot_format
import utils.save_test_figs as stf

def sep_t(dumpfile_list, progress=False):
    if type(dumpfile_list) == str:
        dumpfile_list = [dumpfile_list]  
    time = np.array([])
    x_sep, y_sep, z_sep = np.array([]), np.array([]), np.array([])
    r_sep = np.array([])
    for dump in dumpfile_list:
        file_name = dump.split('/',-1)[-1]
        sdf, sdf_sinks = sar.read_phantom(dump)
        x_sinks = sdf_sinks['x'][1] - sdf_sinks['x'][0]
        y_sinks = sdf_sinks['y'][1] - sdf_sinks['y'][0]
        z_sinks = sdf_sinks['z'][1] - sdf_sinks['z'][0]
        r = np.sqrt(x_sinks**2 + y_sinks**2 + z_sinks**2)
        x_sep, y_sep, z_sep = np.append(x_sep,x_sinks) , np.array(y_sep,y_sinks), np.array(z_sep,z_sinks)
        r_sep = np.append(r_sep,r)
        time = np.append(time,sdf.params['time'])
        if progress == True:
            print('Orbital separation calculation of file: ',file_name)
    
    return time, x_sep, y_sep, z_sep, r_sep


if __name__ == "__main__":
    yr = constants.yr
    path_dumpfiles, path_save = './data/CE_example/', './'    
    if len(sys.argv) > 1:
        path_dumpfiles = sys.argv[1] + '/'
        path_save = sys.argv[-1] + '/'    
    dump_list = read_dumpfiles(path=path_dumpfiles)
    time, x_sep, y_sep, z_sep, r_sep = sep_t(dump_list,progress=True)
    plt.plot(time*yr,r_sep)
    plot_format('time [yr]', 'Orbital separation [$R_{\odot}$]',leg=False)
    stf.make_fig_dir(path_save)
    save_figure(path_save + 'figs/separation.pdf')
