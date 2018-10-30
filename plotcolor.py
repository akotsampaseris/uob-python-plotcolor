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
nano = 1e9

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
r_p = np.unique(r_p)*nano
wavelength = np.unique(wavelength)*nano

# Initialize the absorption sigma matrix
abs_sigma_matrix = [[0 for x in range(len(r_p))] for y in range(len(wavelength))]
scat_sigma_matrix = [[0 for x in range(len(r_p))] for y in range(len(wavelength))]
ext_sigma_matrix = [[0 for x in range(len(r_p))] for y in range(len(wavelength))]

for i in range(len(r_p)):
    for j in range(len(wavelength)):
        k = (i)*len(wavelength) + j
        abs_sigma_matrix[i][len(wavelength) - 1 - j] = abs_sigma[k]
        scat_sigma_matrix[i][len(wavelength) - 1 - j] = scat_sigma[k]
        ext_sigma_matrix[i][len(wavelength) - 1 - j] = scat_sigma[k] + abs_sigma[k]

xlabel = 'Wavelength (nm)'
ylabel = 'Particle radius (nm)'

fig1, ax1 = plt.subplots()
cmap1 = 'coolwarm'
title1 = r'Absorption cross section $\sigma_{abs}$'
c1 = ax1.pcolormesh(wavelength, r_p, abs_sigma_matrix, cmap=cmap1)
fig1.colorbar(c1)
plt.title(title1)
plt.xlabel(xlabel)
plt.ylabel(ylabel)

fig2, ax2 = plt.subplots()
cmap2 = 'coolwarm'
title2 = r'Scattering Cross Section $\sigma_{scat}$'
c2 = ax2.pcolormesh(wavelength, r_p, scat_sigma_matrix, cmap=cmap2)
fig2.colorbar(c2)
plt.title(title2)
plt.xlabel(xlabel)
plt.ylabel(ylabel)

fig3, ax3 = plt.subplots()
cmap3 = 'coolwarm'
title3 = r'Extinction Cross Section $\sigma_{ext}$'
c3 = ax3.pcolormesh(wavelength, r_p, ext_sigma_matrix, cmap=cmap3)
fig3.colorbar(c3)
plt.title(title3)
plt.xlabel(xlabel)
plt.ylabel(ylabel)

plt.show()
