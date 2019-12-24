import numpy as np
import pandas as pd


def fetch_data(dx,dy,dz,file):
    data = pd.read_excel(file)
    x = np.zeros((dx,dy,dz), dtype= float)
    col = 0
    row = 0
    for z in range(0,dz):
        for y in range(0,dy):
            for i in range(0,dx):
                x[i][y][z] = data.iloc[row][col]
                col = col + 1
                if col == x:
                    row = row + 1
                    col = 0

    for z in range(0,dz):
        print("z= 0")
        for y in range(0,dy):
            for i in range(0,dx):
                print(x[i][y][z])
            