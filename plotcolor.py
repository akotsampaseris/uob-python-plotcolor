import matplotlib.pyplot as plt, numpy as np
from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator
import csv
from array import array

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


N = 10000
x, y = np.mgrid[:N, :N]
Z = abs_sigma
print(len(abs_sigma))

fig, axs = plt.subplots(2,2)

ax1 = axs[0,0]
c = ax1.imshow(
        Z, cmap='RdBu',
        vmin=-10, vmax=10,
        interpolation='none'
)
fig.colorbar(c, ax=ax1, extend='both')
plt.show()



"""dy, dx = 0.15, 0.15

y, x = np.mgrid[
        slice(min(r_p), max(r_p), dy),
        slice(min(wavelength), max(wavelength), dx)
]
z = abs_sigma
z_min = min(z)
z_max = max(z)

fig, axs = plt.subplots(2, 2)

ax = axs[0,0]
c = ax.pcolormesh(
        x, y, z,
        cmap='PiYG', vmin=z_min, vmax=z_max
)
ax.set_title('pcolor')
ax.axis([
        min(x), max(x),
        min(y), max(y)
])
fig.colorbar(c, ax=ax)

plt.title('Radius of nanoparticle vs wavelength')

plt.legend()

plt.show()
"""
