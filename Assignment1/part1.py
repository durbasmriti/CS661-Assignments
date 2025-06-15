import vtk
from vtk import *
import sys

reader = vtk.vtkXMLImageDataReader()

# interpolate
def interpolate(p1, p2, val1, val2, isovalue):
    t = (isovalue - val1) / (val2 - val1)
    return [p1[i] + t * (p2[i] - p1[i]) for i in range(3)]

def extract_isocontour(image_data, isovalue):
    dims = image_data.GetDimensions()
    # to store points where f(p) = isoval
    points = vtk.vtkPoints()
    # to store lines
    lines = vtk.vtkCellArray()

    point_data = image_data.GetPointData().GetScalars()

    def get_point_id(i, j):
        return j * dims[0] + i

    for j in range(dims[1] - 1):
        for i in range(dims[0] - 1):
            ids = [
                get_point_id(i, j),
                get_point_id(i + 1, j),
                get_point_id(i + 1, j + 1),
                get_point_id(i, j + 1)
            ]
            scalars = [point_data.GetTuple1(pid) for pid in ids]
            coords = [image_data.GetPoint(pid) for pid in ids]

            # Edges: bottom (0-1), right (1-2), top (2-3), left (3-0)
            segments = []
            edge_ids = [(0,1), (1,2), (2,3), (3,0)]
            # Check each edge for intersection with the isovalue
            # If the product of the scalar values at the endpoints is negative, it means the isovalue crosses this edge
            for (a,b) in edge_ids:
                if (scalars[a] - isovalue) * (scalars[b] - isovalue) < 0:
                    pt = interpolate(coords[a], coords[b], scalars[a], scalars[b], isovalue)
                    segments.append(pt)

            if len(segments) == 2:
                id1 = points.InsertNextPoint(segments[0])
                id2 = points.InsertNextPoint(segments[1])
                line = vtk.vtkLine()
                line.GetPointIds().SetId(0, id1)
                line.GetPointIds().SetId(1, id2)
                lines.InsertNextCell(line)

    poly_data = vtk.vtkPolyData()
    poly_data.SetPoints(points)
    poly_data.SetLines(lines)

    return poly_data

# Main function to extract isocontours and write to file
def write_polydata(polydata, output_filename):
    writer = vtk.vtkXMLPolyDataWriter()
    writer.SetFileName(output_filename)
    writer.SetInputData(polydata)
    writer.Write()

if _name_ == "_main_":
    if len(sys.argv) != 3:
        print("Usage: python extract_contour.py <input.vti> <isovalue>")
        sys.exit(1)

    input_vti = sys.argv[1]
    isovalue = float(sys.argv[2])
    output_vtp = "isocontour_output.vtp"

    # Use the reader already defined above, or define a function to load image data if needed
    # Here, we use the reader from above for simplicity
    reader.SetFileName(input_vti)
    reader.Update()
    image_data = reader.GetOutput()
    contour = extract_isocontour(image_data, isovalue)
    write_polydata(contour, output_vtp)

    print(f"Isocontour extracted and saved to {output_vtp}")


