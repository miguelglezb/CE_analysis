# Separation module   

[Separation](../src/separation.py) module calculates orbital separation of the sink particles for each moment in the simulation 

``sep_t(dumpfile_list, progress=False)``

    Calculates the separation of the sink particles in x,y and z axis. 
    It also calculates the total separation between them
    Parameter 
    ----------
    dumpfile_list : list of paths of the dumpfiles of the simulation 
    progress : boolean, default=False   
    if True, prints the name of file that is using from the simulation for the kinetic energy calculation.

    Returns
    -------
    Five arrays of floats with time and x,y,z and total orbital separations.