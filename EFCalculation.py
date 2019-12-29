#This script performs essential statistical analysis
import numpy as np 
import pyvista

def get_x_coordinate(coordinate_vector, index):
    return coordinate_vector[index][0]

def get_y_coordinate(coordinate_vector, index):
    return coordinate_vector[index][1]

def get_z_coordinate(coordinate_vector, index):
    return coordinate_vector[index][2]