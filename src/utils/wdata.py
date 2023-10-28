#!/usr/bin/python3
# -*- coding: utf-8 -*-

def write_hist2D_data(xdata,ydata,x_name,y_name,pmass,pathfile,filename='hist2D_data.txt'):
    f = open(pathfile+filename,'w')
    column_names = x_name + '\t' + y_name + '\n'
    f.write("# Particle mass: " + str(pmass)+ '\n')
    f.write(column_names)
    for x,y in zip(xdata,ydata):
        line = str(round(x,3)) + "\t" + str(round(y,3)) + '\n'
        f.write(line)
    
    f.close()        
