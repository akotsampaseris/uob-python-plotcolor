import numpy as np

from functions import *

# Define the names of the files
files = [
        {'name': 'AbsorptionXSection', 'type': '.csv'},
        {'name':'ScatteringXSection', 'type': '.csv'}
]

# Define variables
variables = ['r_p', 'wavelength', 'abs_sigma', 'scat_sigma']

# Get data from files
for entry in files:
    path='data/' + entry['name'] + entry['type']
    r_p, wavelength, abs_sigma = getdata(path, 'r_p')


r_p = np.unique(r_p)
wavelength = np.unique(wavelength)

abs_sigma_matrix = [[0 for x in range(len(r_p))] for y in range(len(wavelength))]

for i in range(len(r_p)):
    for j in range(len(wavelength)):
        k = (i)*len(wavelength) + j
        abs_sigma_matrix[j][len(r_p)-1-i] = abs_sigma[k]
"""
#plotcolormesh(wavelength, r_p, abs_sigma_matrix)
