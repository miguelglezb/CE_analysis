#!/usr/bin/python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc
from matplotlib import rcParams
import sarracen as sar
from separation import sep_t
from utils.rdumpfiles import read_dumpfiles
from utils.vector_math import recentre_from_sink
from utils.units import constants
from utils.pformat import save_figure,plot_format

def p_soft(q):
    '''
    M-4 kernel for modified potential close to sink particle        
    
    Parameter 
    ----------
    q : q=r/h ratio between sink-gas particle and h=max(hsoft,hi) 
    where hsoft in the sink softening length and hi is the sph particle
    smoothing length

    Returns
    -------
    float, list, pandas.series (same type as q)

    '''
    coefs = [105/32768, -11/256, 1925/8192, -165/256, 825/1024, -231/256, 165/128, -55/32]
    p_soft = 105.*np.power(q,10)/32768. - 11.*np.power(q,9)/256. + 1925.*np.power(q,8)/8192. 
    p_soft = p_soft - 165.*np.power(q,7)/256. + 825.*np.power(q,6)/1024. - 231.*np.power(q,4)/256. 
    p_soft = p_soft + 165.*np.power(q,2)/128. - 55./32.
    return p_soft

def sink_gas_potential(m_sink,h_isoft,r):
    '''
    Grav. potential function (both newtonian and modified adapted for pandas series)    

    Parameter 
    ----------
    m_sink : mass of sink particle 
    
    Returns
    -------
    float, list, pandas.series (same type as q)
    '''
    q = r/h_isoft
    p_lowq = p_soft(q)*m_sink/h_isoft
    p_highq = -m_sink/r
    pot = p_lowq.where(q<2,p_highq)
    return pot

# Calculation of gravitational potential energy for the entire envelope 
# (assuming 2 sink particles and )
def tot_potential(dumpfile_list):
    '''
    Calculation of total gravitational potential energy in the common envelope,
    including sink-sink, sink-gas and gas-gas potential over time.    
    
    Parameter 
    ----------
    dumpfile_list : list
       list of paths of the dumpfiles of the simulation 

    Returns
    -------
    Two arrays of floats with time and total potential energies.

    '''
    time = np.array([])
    potential = np.array([])
    for dump in dumpfile_list:
        file_name = dump.split('/',-1)[-1]
        sdf, sdf_sinks = sar.read_phantom(dump)
        particlemass = sdf.params['mass']
        [x1, y1, z1] = recentre_from_sink(sdf,sdf_sinks,sink=0)
        [x2, y2, z2] = recentre_from_sink(sdf,sdf_sinks,sink=1)
        x_sinks = sdf_sinks['x'][1] - sdf_sinks['x'][0]
        y_sinks = sdf_sinks['y'][1] - sdf_sinks['y'][0]
        z_sinks = sdf_sinks['z'][1] - sdf_sinks['z'][0]
        r_sinks = np.sqrt(x_sinks**2 + y_sinks**2 + z_sinks**2)
        r1 = np.sqrt(np.square(x1) + np.square(y1) + np.square(z1))
        r2 = np.sqrt(np.square(x2) + np.square(y2) + np.square(z2))
        sdf['hs1'] = sdf['h'].where(sdf['h'] > sdf_sinks['hsoft'][0], sdf_sinks['hsoft'][0])
        sdf['hs2'] = sdf['h'].where(sdf['h'] > sdf_sinks['hsoft'][1], sdf_sinks['hsoft'][1])
        phi1 = sink_gas_potential(sdf_sinks['m'][0],sdf['hs1'],r1).sum()
        phi2 = sink_gas_potential(sdf_sinks['m'][1],sdf['hs2'],r2).sum()
        pot_bet_sinks = -(sdf_sinks['m'][0]*sdf_sinks['m'][1])/r_sinks
        tot_pot = particlemass*(phi1 + phi2) + sdf['poten'].sum() + pot_bet_sinks
        potential = np.append(potential, tot_pot)
 
        time = np.append(time,sdf.params['time'])
        print('file: ',file_name)
    return time, potential

def tot_kinetic(dumpfile_list):
    '''
    Calculation of total kinetic energy in the common envelope, including 
    sink-sink, sink-gas and gas-gas potential over time        
    
    Parameter 
    ----------
    dumpfile_list : list
       list of paths of the dumpfiles of the simulation 

    Returns
    -------
    Two arrays of floats with time and total kinetic energies.
    '''

    time = np.array([])
    kinetic = np.array([])
    for dump in dumpfile_list:
        file_name = dump.split('/',-1)[-1]
        sdf, sdf_sinks = sar.read_phantom(dump)
        particlemass = sdf.params['mass']
        v2_sink1 = sdf_sinks['vx'][0]**2 + sdf_sinks['vy'][0]**2 + sdf_sinks['vz'][0]**2
        v2_sink2 = sdf_sinks['vx'][1]**2 + sdf_sinks['vy'][1]**2 + sdf_sinks['vz'][1]**2
        v2_gas = np.sum(sdf['vx']**2 + sdf['vy']**2 + sdf['vz']**2)
        kin = 0.5*(particlemass*v2_gas + sdf_sinks['m'][0]*v2_sink1 + sdf_sinks['m'][1]*v2_sink2)
        kinetic = np.append(kinetic, kin)

        time = np.append(time,sdf.params['time'])
        print('file: ',file_name)
    return time, kinetic


def tot_kinetic_parts(dump):
    sdf, sdf_sinks = sar.read_phantom(dump)
    particlemass = sdf.params['mass']
    v2_gas = sdf['vx']**2 + sdf['vy']**2 + sdf['vz']**2
    kin = 0.5*particlemass*v2_gas
    time = sdf.params['time']
    return time, kin

def tot_potential_parts(dump):
    sdf, sdf_sinks = sar.read_phantom(dump)
    particlemass = sdf.params['mass']
    [x1, y1, z1] = recentre_from_sink(sdf,sdf_sinks,sink=0)
    [x2, y2, z2] = recentre_from_sink(sdf,sdf_sinks,sink=1)
    r1 = np.sqrt(np.square(x1) + np.square(y1) + np.square(z1))
    r2 = np.sqrt(np.square(x2) + np.square(y2) + np.square(z2))
    sdf['hs1'] = sdf['h'].where(sdf['h'] > sdf_sinks['hsoft'][0], sdf_sinks['hsoft'][0])
    sdf['hs2'] = sdf['h'].where(sdf['h'] > sdf_sinks['hsoft'][1], sdf_sinks['hsoft'][1])
    phi1 = sink_gas_potential(sdf_sinks['m'][0],sdf['hs1'],r1)
    phi2 = sink_gas_potential(sdf_sinks['m'][1],sdf['hs2'],r2)
    pot = particlemass*(phi1 + phi2) + sdf['poten'] 
    time = sdf.params['time']
    return time, pot



if __name__ == "__main__":
    yr = constants.yr
    erg = constants.ener
    path_dumpfiles = 'data/CE_example/'
    dump_list = read_dumpfiles(path=path_dumpfiles)
    time, sink_potential = tot_potential(dump_list)
    plt.plot(time*yr, sink_potential*erg)
    plot_format('yr', 'Bound mass [erg]',leg=False)
    plt.show()
    

