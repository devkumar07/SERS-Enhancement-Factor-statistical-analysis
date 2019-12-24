import numpy as np
import pandas as pd

data = pd.read_excel('data.xlsx')
print(data.iloc[0,2])

x = np.zeros((3,3,3), dtype= float)
col = 0
row = 0
for z in range(0,3):
    for y in range(0,3):
        for i in range(0,3):
            x[i][y][z] = data.iloc[row][col]
            col = col + 1
            if col == 9:
                row = row + 1
                col = 0

for z in range(0,3):
    print("z= 0")
    for y in range(0,3):
        for i in range(0,3):
            print(x[i][y][z])
        