# User guide

### [Home](./index.md)

## How to run
From the main CE_analysis directory, type 

```python3 src/energies.py CE_DIR CE_figs``` 

to use the dumpfiles stored in `CE_DIR` directory to generate the mechanical energy plot in `CE_figs`. 

Type:

```python3 src/separation.py CE_DIR CE_figs``` 

to create the separation plots. If `CE_figs` is not given, the plots will be saved in `CE_DIR/figs/`

**Warning:** dumpfiles must be named with the prefix `binary_`. That is, `CE_figs` must contain `binary_00000`, `binary_00001`, etc. Future versions will allow for customizable naming conventions

## Uninstallation of LaTeX packages
LaTeX packages installed for CE_analysis can be uninstall by typing:

```sudo make uninstall_latex_dependencies``` 