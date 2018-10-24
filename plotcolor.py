import matplotlib.pyplot as plt, numpy as np
import csv

# Define the names of the files
filenames = ['AbsorptionXSection', 'ScatteringXSection']
filename = 'AbsorptionXSection'
extension = ".csv"

# Define variables
r_p = []
wavelength = []
abs_sigma = []
scat_sigma = []

# Open the csv files to read the data
with open('data/'+filename+extension, 'r') as csvfile:
    data = csv.DictReader(csvfile)

    for row in data:
        r_p.append(float(row['r_p']))
        wavelength.append(float(row['wavelength']))
        abs_sigma.append(float(row['abs_sigma']))


r_p = np.unique(r_p)
wavelength = np.unique(wavelength)

abs_sigma_matrix = [[0 for x in range(len(r_p))] for y in range(len(wavelength))]

for i in range(len(r_p)):
    for j in range(len(wavelength)):
        k = (i)*len(wavelength) + j
        abs_sigma_matrix[j][len(r_p)-1-i] = abs_sigma[k]

x = wavelength
y = r_p
z = abs_sigma_matrix
print(x)

fig, ax = plt.subplots()
cs = ax.pcolormesh(x, y, z, cmap='RdBu')
fig.colorbar(cs)
ax.set_title("Test")
plt.show()
