# Energies module   

[Energies](../src/energies.py) module calculates several types of energies of the CE simulation. With a few exceptions, it will also save the time (in *Phantom* units) of the simulation at that moment.  

``sink_gas_potential(m_sink,h_isoft,r):``

    
    Gravity potential function (both newtonian and modified adapted for pandas series)    

    Parameter 
    ----------
    m_sink : float, mass of sink particle 
    h_isoft : float, softening length of sink particle
    r : ndarray, distance from sink to each SPH (gas) particle
    
    Returns
    -------
    float, list, pandas.series (same type as q)
    

``p_soft(q)``

    M-4 kernel for modified potential close to sink particle        
    
    Parameter 
    ----------
    q : q=r/h ratio between sink-gas particle and h=max(hsoft,hi) 
    where hsoft in the sink softening length and hi is the sph particle
    smoothing length

    Returns
    -------
    float, list, pandas.series (same type as q)

``tot_potential(dumpfile_list, progress=False)``

    Calculation of total gravitational potential energy in the common envelope,
    including sink-sink, sink-gas and gas-gas potential over time.    
    
    Parameter 
    ----------
    dumpfile_list : list
        list of paths of the dumpfiles of the simulation 
    progress : boolean, default=False   
        if True, prints the name of file that is using from the simulation for the kinetic energy calculation.

    Returns
    -------
    Two arrays of floats with time and total potential energies.


``tot_kinetic(dumpfile_list, progress=False)``

    Calculation of total kinetic energy in the common envelope, including 
    sink-sink, sink-gas and gas-gas potential over time        
    
    Parameter 
    ----------
    dumpfile_list : list
       list of paths of the dumpfiles of the simulation 
    progress : boolean, default=False   
        if True, prints the name of file that is using from the simulation for the kinetic energy calculation.
    Returns
    -------
    Two arrays of floats with time and total kinetic energies.

``tot_kinetic_gas(dump)``

    Calculation of total kinetic energy of the gas for a single dumpfile
    
    Parameters
    ----------
    dump : str, name (path included) of the dumpfile

    Returns
    -------
    Two arrays of floats with time and gas kinetic energy.

``total_mechanical(kinetic_energy, potential_energy)``

    Adds total kinetic and total mechanic energies from the gas
        
    Parameters
    ----------
    kinetic_energy : float, kinetic energy of the gas 
    potential_energy : float, potential energy of the gas 

    
    Returns
    -------
    float, total mechanical energy of the gas
