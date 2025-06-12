import vtk
from vtk import *

# load the dataset
reader = vtk.vtkXMLImageDataReader()
reader.SetFileName(r"C:\\Users\\durba\\Downloads\\vtk_practice\\CS661-Assignments\\Assignment1\\Isabel_2D.vti")
reader.Update()
data = reader.GetOutput()

# take user input
isoval = int(input("Enter the isovalue: "))

# have to store isolines and points p where f(p) = isovalue
# maintain a vtkCellArray object and later add it to vtkPolyData


# Traverse the grid cells
def traverse():
    '''
    Input: a single cell
    Traverse a single cell in counter clockwise order
    return active edges
    '''

# interpolate
def interpolation():
    '''
    Input : active edge from traverse() func
    found p where f(p) = isovalue
    output : join the p with existing isoline
    '''

# Use vtkXMLPolyDataWriter to write the .vtp file