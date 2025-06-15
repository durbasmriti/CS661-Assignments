Part 1 of Assignment_1 (part1.py):
-------

This script extracts the isocontour from a 2D scalar field in VTI format.

Dataset:
-------

 Isabel_2D.vti

Run the script:
-------

To run the script, use the following command from terminal:

    python <path to part1.py script> <input_file.vti> <isovalue>

Output:
-------
- This will create an output file named isocontour_output.vtp in the same directory.
- This can be visualized in ParaView


Part 2 of  Assignment_1 (part2.py):
-------

Dataset:
-------
Isabel_3D.vti

Set the filename correct:

reader.SetFileName(r"C:\\Users\\durba\\Downloads\\vtk_practice\\CS661-Assignments\\Assignment1\\Isabel_3D.vti")

Modify this line according to the path of Isabel_3D.py in your directory (Note: Use double slash in the directory name)

Run the script:
-------

    python <path to part2.py>

Instructions:
-------
    - Make sure Isabel_3D.vti is present in the same path as mentioned in the script.
    - When prompted, type 'yes' to enable Phong shading, 'no' to disable it.

Output:
-------
- A 1000x1000 render window will appear showing the volume-rendered dataset.
- The redered image will be as per your choice of shading or no shading.





Author:
-------
Durbasmriti Saha

Mohd Fahad

Pratiksha Dawane

Course: CS661 - Big Data Analytics (IITK)
