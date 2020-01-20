import tkinter as tk
from tkinter import filedialog, messagebox
from VTKReader import *
from EFCalculation import *

def resultMessage(message):
    popup = tk.Toplevel()
    popup.title("Result")
    label = tk.Label(popup, text=message) #Can add a font arg here
    label.pack(side="top", fill="x", pady=10)
    B1 = tk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()

def execute(event=None):
    f_name = 'Data/'+filename.get()
    data = read_vtk(f_name)
    coordinates = get_coordinates_vector(data)
    coordinates = convert_to_nm(coordinates)
    EField = get_electric_field_vector(data)
    EF = fetch_EF_from_surface_trimer(EField,coordinates,small_radius.get(),big_radius.get(),gap_junction.get())
    message = 'Max = '+str(max(EF))+'\n Mean = '+str(calculate_average_EF(EF))+'\n Median = '+str(calculate_median_EF(EF))+'\n Standard Deviation = '+str(calculate_standard_deviation_EF(EF))
    resultMessage(message)

master = tk.Tk()

tk.Label(master, text="Enter the name of the VTR file").grid(row=0)
tk.Label(master, text="Radius of Center Particle").grid(row=1)
tk.Label(master, text="Radius of Big Particles").grid(row=2)
tk.Label(master, text="Gap Junction").grid(row=3)

filename = tk.Entry(master)
filename.grid(row=0, column=1)
small_radius = tk.Entry(master)
small_radius.grid(row=1, column=1)
big_radius = tk.Entry(master)
big_radius.grid(row=2, column=1)
gap_junction = tk.Entry(master)
gap_junction.grid(row=3, column=1)

tk.Button(master, text='Quit', command=master.quit).grid(row=4, column=0, sticky=tk.W, pady=4)
tk.Button(master, text='Perform analysis', command=execute).grid(row=4, column=1, sticky=tk.W, pady=4)

tk.mainloop()