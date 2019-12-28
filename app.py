import numpy as np
import pyvista
from VTKReader import *

vtkInput = 'Data/'+input('Enter the VTK file input: ')

data = read_vtk(vtkInput)

coordinates = get_coordinates_vector(data)

EField = get_electric_field(data)

print(coordinates)

print(EField)