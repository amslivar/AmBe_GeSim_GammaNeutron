# Read the spectrum data from the file
file_name = '/mnt/raid5/users/amslivar/AmBe_work/AmBe_v2/AmBe_neutron_gamma_spec/AmBe_SOURCES4A_n2_neutron.spectrum'
spectrum = []

with open(file_name, 'r') as file:
    for line in file:
        energy, branching_ratio = map(float, line.split())
        spectrum.append((energy, branching_ratio))

# Calculate the sum of all branching ratios
total_branching_ratio = sum([br for _, br in spectrum])

# Normalize the branching ratios
normalized_spectrum = [(energy, br / total_branching_ratio) for energy, br in spectrum]

# Save the normalized spectrum to a new file
output_file_name = '/mnt/raid5/users/amslivar/AmBe_work/AmBe_v2/AmBe_neutron_gamma_spec/AmBe_SOURCES4A_n2_neutron_normalized.spectrum'
with open(output_file_name, 'w') as output_file:
    for energy, normalized_br in normalized_spectrum:
        output_file.write("{:.2f}\t{:.8E}\n".format(energy, normalized_br))

print("Normalized spectrum saved to {}".format(output_file_name))
