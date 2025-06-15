# CS661 - Assignment 1 - Part 2
import vtk
from vtk import *

# Loading the data
reader = vtk.vtkXMLImageDataReader()
reader.SetFileName(r"C:\\Users\\durba\\Downloads\\vtk_practice\\CS661-Assignments\\Assignment1\\Isabel_3D.vti")
reader.Update()

# Color transfer function
colorTF = vtk.vtkColorTransferFunction()
colorTF.AddRGBPoint(-4931.54, 0, 1, 1)
colorTF.AddRGBPoint(-2508.95, 0, 0, 1)
colorTF.AddRGBPoint(-1873.9, 0, 0, 0.5)
colorTF.AddRGBPoint(-1027.16, 1, 0, 0)
colorTF.AddRGBPoint(-298.031, 1, 0.4, 0)
colorTF.AddRGBPoint(2594.97, 1, 1, 0)

# Opacity transfer function
opacityTF = vtk.vtkPiecewiseFunction()
opacityTF.AddPoint(-4931.54, 1.0)
opacityTF.AddPoint(101.815, 0.002)
opacityTF.AddPoint(2594.97, 0.0)

# Volume rendering
volumeMapper = vtk.vtkSmartVolumeMapper()
volumeMapper.SetInputData(reader.GetOutput())

# Volume property
volumeProperty = vtk.vtkVolumeProperty()
volumeProperty.SetColor(colorTF)
volumeProperty.SetScalarOpacity(opacityTF)

# Phong shading?
usePhong = input("Do you want to use Phong shading? (yes/no) ").strip().lower()
if usePhong == "yes":
    volumeProperty.ShadeOn()
    volumeProperty.SetAmbient(0.5)
    volumeProperty.SetDiffuse(0.5)
    volumeProperty.SetSpecular(0.5)
else:
    volumeProperty.ShadeOff()

# Volume, and setting the mapper and property
volume = vtk.vtkVolume()
volume.SetMapper(volumeMapper)
volume.SetProperty(volumeProperty)

# Adding an outline
outline = vtk.vtkOutlineFilter()
outline.SetInputData(reader.GetOutput())
outlineMapper = vtk.vtkPolyDataMapper()
outlineMapper.SetInputConnection(outline.GetOutputPort())
outlineActor = vtk.vtkActor()
outlineActor.SetMapper(outlineMapper)

# Render window
renderer = vtk.vtkRenderer()
renderer.AddVolume(volume)
renderer.AddActor(outlineActor)

renWindow = vtk.vtkRenderWindow()
renWindow.SetSize(1000, 1000)
renWindow.AddRenderer(renderer)

windowInteractor = vtk.vtkRenderWindowInteractor()
windowInteractor.SetRenderWindow(renWindow)

# Interaction
windowInteractor.Initialize()
renWindow.Render()
windowInteractor.Start()
