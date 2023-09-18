#!/usr/bin/python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import dataread as dr

def recentre_from_sink(sdf,sdf_sinks,columns=['x','y','z'],sink=0):
    rct = []
    for i in columns:
        rct.append(sdf[i] - sdf_sinks[i][sink])
    return rct
