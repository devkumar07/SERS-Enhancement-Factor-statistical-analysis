#This is the main program to run 
import numpy as np
import pyvista
from VTKReader import *
from EFCalculation import *

vtkInput = 'Data/'+input('Enter the VTK file input: ')

data = read_vtk(vtkInput)

coordinates = get_coordinates_vector(data)

EField = get_electric_field_vector(data)

print(coordinates)

print(get_x_coordinate(coordinates,2))

print(EField)

data.plot(show_grid=True)