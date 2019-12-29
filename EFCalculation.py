#This script performs essential statistical analysis
import numpy as np 
import pyvista
import math

def get_x_coordinate(coordinate_vector, index):
    return coordinate_vector[index][0]

def get_y_coordinate(coordinate_vector, index):
    return coordinate_vector[index][1]

def get_z_coordinate(coordinate_vector, index):
    return coordinate_vector[index][2]

def radius_threshold(x,y,radius):
    r = math.floor(math.sqrt(x**2 + y**2))
    if r == radius:
        return True
    return False
def get_z_interval(intensity_vector):
    return int(len(intensity_vector)**(1./3))

def convert_to_nm(coordinate_vector):
    for i in range(0,len(coordinate_vector)):
        coordinate_vector[i] = coordinate_vector[i] * 1000
    return coordinate_vector