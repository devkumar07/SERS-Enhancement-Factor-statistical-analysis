#This is the main program to run 
import numpy as np
import pyvista
from VTKReader import *
from EFCalculation import *

vtkInput = 'Data/'+input('Enter the VTK file input: ')

radius = input('Enter the radius of the structure: ')

data = read_vtk(vtkInput)

coordinates = get_coordinates_vector(data)

EField = get_electric_field_vector(data)

coordinates = convert_to_nm(coordinates)

print(coordinates)

print(EField)

EF = fetch_EF_from_surface(EField,coordinates,radius)

print('EFs: ',EF)


print('Mean = ', calculate_average_EF(EF))
print('Median = ',calculate_median_EF(EF))
print('Standard Deviation = ',calculate_standard_deviation_EF(EF))

