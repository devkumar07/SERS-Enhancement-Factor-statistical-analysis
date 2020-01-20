#This script has functions to read VTK files
import pyvista

def read_vtk(file_name):
    return pyvista.read(file_name)

def get_coordinates_vector(data):
    return data.points

def get_electric_field_vector(data):
    return data.point_arrays['Intensity']