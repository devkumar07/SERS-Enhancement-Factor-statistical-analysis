#This script performs essential statistical analysis
import numpy as np 
import pyvista
import math
import statistics

def get_x_coordinate(coordinate_vector, index):
    return coordinate_vector[index][0]

def get_y_coordinate(coordinate_vector, index):
    return coordinate_vector[index][1]

def get_z_coordinate(coordinate_vector, index):
    return coordinate_vector[index][2]

#TODO: need to incorporate for the center of the spheres
def radius_threshold(x,y,z,radius):
    r = round(math.sqrt(x**2 + y**2 + z**2),2)
    if r == float(radius):
        return True
    else:
        return False

def convert_to_nm(coordinate_vector):
    for i in range(0,len(coordinate_vector)):
        coordinate_vector[i] = coordinate_vector[i] * 1000
    return coordinate_vector

def fetch_EF_from_surface(intensity_vector, coordinate_vector, radius):
    EF = []
    for i in range(0,len(coordinate_vector)):
        x = get_x_coordinate(coordinate_vector,i)
        y = get_y_coordinate(coordinate_vector,i)
        z = get_z_coordinate(coordinate_vector,i)
        check = radius_threshold(x,y,z,radius)
        if check == True:
            EF.append(intensity_vector[i])
    EF = enhance_electric_field(EF)
    return EF

def enhance_electric_field(EF):
    for i in range(0,len(EF)):
        EF[i] = EF[i]**4
    return EF

def calculate_average_EF(EF):
    return statistics.mean(EF)

def calculate_median_EF(EF):
    return statistics.median(EF)

def calculate_standard_deviation_EF(EF):
    return statistics.stdev(EF)
