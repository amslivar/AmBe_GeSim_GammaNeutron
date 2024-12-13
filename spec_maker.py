## Written by Ana Maria Slivar


### This script reads the energies and probabilities list form different files and creates a new file 
### with the energies and probabilities in the format required by Geant4 under the AmBe_emergent_gammas/am241.cc script 



#### python spec_maker.py <energies_file> <probabilities_file> <output_file>
#### python spec_maker.py /mnt/raid5/users/amslivar/AmBe_work/AmBe_v2/AmBe_neutron_gamma_spec/AmBe_SOURCES4A_n0_neutronEnergy.dat /mnt/raid5/users/amslivar/AmBe_work/AmBe_v2/AmBe_neutron_gamma_spec/AmBe_SOURCES4A_n0_neutronCDF.dat /mnt/raid5/users/amslivar/AmBe_work/AmBe_v2/AmBe_neutron_gamma_spec/AmBe_SOURCES4A_n0_neutron.spectrum

import numpy as np
import os
import sys
# Get the input file names from the command line arguments
if len(sys.argv) != 4:
    print("Usage: python spec_maker.py <energies_file> <probabilities_file> <output_file>")
    sys.exit(1)

energies_file = sys.argv[1]
probabilities_file = sys.argv[2]
output_file = sys.argv[3]

# Read the energies and probabilities from the files
energies = np.loadtxt(energies_file)
probabilities = np.loadtxt(probabilities_file)

# Create the new file in the format energy probability eg "921.5	1.9E-07"

with open(output_file, 'w') as f:
    for i in range(len(energies)):
        f.write('{} {}\n'.format(energies[i], probabilities[i]))
        
print('The file {} has been created'.format(output_file))
