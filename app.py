#This is the main program to run 
from VTKReader import *
from EFCalculation import *

vtkInput = '/Users/dev/Desktop/MACES/SERS-Enhancement-Factor-statistical-analysis/Data/Trimer.vtr'

small_radius = input('Enter the small radius of the structure: ')

big_radius = input('Enter the big radius of the structure: ')

gap = input('Enter the gap junction of the structure: ')

data = read_vtk(vtkInput)

coordinates = get_coordinates_vector(data)

EField = get_electric_field_vector(data)

print(max(EField))

coordinates = convert_to_nm(coordinates)

print(coordinates)

#print(len(EField))


EF = fetch_EF_from_surface_trimer(EField,coordinates,small_radius,big_radius,gap)

print('EFs: ',EF)

print('Max = ',max(EF))
print('Mean = ', calculate_average_EF(EF))
print('Median = ',calculate_median_EF(EF))
print('Standard Deviation = ',calculate_standard_deviation_EF(EF))
