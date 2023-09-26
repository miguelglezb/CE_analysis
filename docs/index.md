

CE analysis - Analysis tool for common envelope simulations in Phantom
=======================================================

About
-----
CE analysis is a free and open source tool to generate simple analysis of common envelope simulations generated in the hydro 3D code [Phantom](https://ui.adsabs.harvard.edu/abs/2018PASA...35...31P/abstract) created by Daniel J Price. 

Data is read *directly* from the snapshots files (written in binary and with Big Endian format) using the Python3 module [sarracen](https://github.com/ttricco/sarracen/) to create plots of global quantities, such as orbital separation and porcentage of ejected envelope.    

CE analysis uses the SPH smoothing kernel to calculate physical quantities, giving a proper representation of the data. The goal is to produce nice plots and visualisations from the SPH output. 

CE analysis also generates ascii files corresponding to the created plots.

## Contents

-[Getting started](./getting_started.md)

-[User guide](./user_guide.md)

-[API](./api.md)
