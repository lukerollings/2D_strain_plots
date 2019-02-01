# 2D_strain_plots
Reads text files containing a 2D array of d-spacing values from XRD measurements. Returns individual line plots of d-spacing, strain or interfacial shear stress, followed by a 2D strain map. Intended for analysis of strained fibre composites.

Use:

Reads files formatted as "XXXXX_FittingResults.txt", where XXXXX is your scan identification number.
Change the top variables (scan_id, E (stiffness, MPa), r (fibre radius, mm) and d_o (unstrained d-spacing, Angstrom)) to fit your needs.

1st commit:
The parameter that is plotted depends what is entered in the "plt.scatter" command. 
d-spacing = "d"
Strain = "e"
Interfacial Shear Stress = "tau"

2D map only plots d-spacing
