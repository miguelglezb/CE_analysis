#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
from pandas import unique

def read_dumpfiles(files_prefix='binary_', path='./',evy_files=-1):
    '''
    Creates a list of the dumpfiles that will be used in the analysis.
        
    Parameters
    ----------
    files_sufix : str, default='binary_'
        Prefix of the dumpfiles  
    path : str, default='./'
        Path of the dumpfiles
    evy_files : integer, default='-1'
        If -1, it will take the path of every single dumpfile with
        files_sufix in the path. For any other positive integer, it
        will take every evy_files to generate the list
        
    Returns
    -------
    List of strings (dumpfile names, including path)

    '''
    os.system('ls ' + path + files_prefix + '* > listfiles.txt')
    openlist = open('listfiles.txt')
    list_dumpfiles = openlist.read().splitlines() 
    list_dumpfiles = [namefile.rstrip('.divv') for namefile in list_dumpfiles]
    list_dumpfiles = list(unique(list_dumpfiles))
    openlist.close()
    os.system('rm listfiles.txt')          
    if (evy_files == -1) or (evy_files ==  None):
        return list_dumpfiles
    elif evy_files > 0:
        return list_dumpfiles[::evy_files]
    else:
        print("Invalid option for evy_files.")