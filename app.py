#This is the main program to run 
import numpy as np
import pyvista
from VTKReader import *
from EFCalculation import *

vtkInput = 'Data/'+input('Enter the VTK file input: ')

radius = input('Enter the radius of the structure: ')

mesh_size = input('Enter the mesh size: ')

data = read_vtk(vtkInput)

coordinates = get_coordinates_vector(data)

EField = get_electric_field_vector(data)

coordinates = convert_to_nm(coordinates)

print(coordinates)

print(get_x_coordinate(coordinates,2))

print(EField)
