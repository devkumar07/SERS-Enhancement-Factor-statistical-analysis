import numpy as np
import pyvista
data = pyvista.read('Data/ElectricField3DField.vtk')

# Get points as NumPy array
print(data['-0.0005 -0.0005 -0.0005'])
points = data.points
print(points)
print(data.field_arrays)
print(data.point_arrays['Intensity'])
print(data.plot(show_grid=True))