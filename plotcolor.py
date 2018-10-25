import numpy as np, csv
from tkinter import *
from functions import *

filename1 = 'AbsorptionXSection.csv'
filename2 = 'ScatteringXSection.csv'

# Variables
r_p = []
wavelength = []
abs_sigma = []
scat_sigma = []

# Get data from file1
path = 'data/'+ filename1
with open(path, 'r') as csvfile:
    data = csv.DictReader(csvfile)
    for row in data:
        r_p.append(float(row['r_p']))
        wavelength.append(float(row['wavelength']))
        abs_sigma.append(float(row['abs_sigma']))
    csvfile.close()

path = 'data/'+ filename2
with open(path, 'r') as csvfile:
    data = csv.DictReader(csvfile)
    for row in data:
        scat_sigma.append(float(row['scat_sigma']))
    csvfile.close()

# Keep only unique values for the radius and the wavelength
r_p = np.unique(r_p)
wavelength = np.unique(r_p)

# Initialize the absorption sigma matrix
abs_sigma_matrix = [[0 for x in range(len(r_p))] for y in range(len(wavelength))]
scat_sigma_matrix = [[0 for x in range(len(r_p))] for y in range(len(wavelength))]
for i in range(len(r_p)):
    for j in range(len(wavelength)):
        k = (i)*len(wavelength) + j
        abs_sigma_matrix[j][len(r_p) - i - 1] = abs_sigma[k]
        scat_sigma_matrix[j][len(r_p) - i - 1] = scat_sigma[k]

#plotcolormesh(wavelength, r_p, abs_sigma_matrix)
fig1, ax1 = plt.subplots()
cmap1 = 'RdBu'
title1 = 'Absorption Cross Section'
c1 = ax1.pcolormesh(wavelength, r_p, abs_sigma_matrix, cmap=cmap1)
fig1.colorbar(c1)
ax1.set_title(title1)

fig2, ax2 = plt.subplots()
cmap2 = 'RdBu'
title2 = 'Scattering Cross Section'
c2 = ax2.pcolormesh(wavelength, r_p, scat_sigma_matrix, cmap=cmap2)
fig2.colorbar(c2)
ax2.set_title(title2)

plt.show()
