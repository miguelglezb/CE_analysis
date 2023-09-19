#!/usr/bin/python3
# -*- coding: utf-8 -*-

#Conversion of units from Phantom to cgs, day, year... 

class constants:
    mass = 1.989E33 
    time = 1.594E3 
    dist = 6.96E10
    G = 6.67E-8
    vel = dist/time
    dens = mass/dist**3
    spangmom = dist**2/time
    spener = (dist/time)**2
    ener = mass*spener
    angmom = mass*spangmom
    pressure = ener/dist**3 
    yr = time/(24*3600*365)
    day = time/(24*3600)
    hr = time/3600

    def __init__(self,mass=mass,time=time,dist=dist,yr=yr,day=day,
                    spangmom=spangmom,ener=ener,spener=spener,vel=vel,
                    angmom=angmom,dens=dens, pressure=pressure,hr=hr,G=G):
        """Phantom units in cgs"""
        self.G = G 
        self.mass = mass 
        self.time = time 
        self.dist = dist
        self.vel = vel
        self.dens = dens
        self.spangmom = spangmom
        self.spener = spener
        self.angmom = angmom
        self.ener = ener
        self.pressure = pressure
        self.yr = yr 
        self.day = day 
        self.hr = hr
        
