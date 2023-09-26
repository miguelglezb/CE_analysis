CE analysis - Analysis tool for common envelope simulations in Phantom
=======================================================

About
-----
CE analysis is a free and open source tool to generate simple analysis of common envelope simulations generated in the hydro 3D code [Phantom](https://ui.adsabs.harvard.edu/abs/2018PASA...35...31P/abstract) created by Daniel J Price. 

Data is read *directly* from the snapshots files (written in binary and with Big Endian format) using the Python3 module [sarracen](https://github.com/ttricco/sarracen/) to create plots of global quantities, such as orbital separation and porcentage of ejected envelope.    

CE analysis uses the SPH smoothing kernel to calculate physical quantities, giving a proper representation of the data. The goal is to produce nice plots and visualisations from the SPH output. 

CE analysis also generates ascii files corresponding to the created plots.

More information can be found in CE_analysis [documentation](https://miguelglezb.github.io/CE_analysis/) page

# Installation

In the terminal, from the CE_analysis main directory, type:

```sudo make install```

to install all python required modules and latex fonts for the plots

# Test

We include a simple test to check if the code has being installed successfully. This test will use a CE simulation dumpfiles from data/CE_example (if this files are not stored in that directory it will download them, a free space of 5 GB is required for this). The test will create plots of orbital evolution of the binary and mechanical energy of the envelope. To run this test type in the main CE_analysis directory:

```make test```

At the end of the test CE_analysis will confirm the files are saved in the `figs` directory.

# Run

From the main CE_analysis directory, type 

```python3 src/energies.py CE_DIR CE_figs``` 

to use the dumpfiles stored in `CE_DIR` directory to generate the mechanical energy plot in `CE_figs`. 

Type:

```python3 src/separation.py CE_DIR CE_figs``` 

to create the separation plots. If `CE_figs` is not given, the plots will be saved in `CE_DIR/figs/`