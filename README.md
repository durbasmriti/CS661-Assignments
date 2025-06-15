README - 2D Isocontour Extraction

This script extracts the isocontour from a 2D scalar field in VTI format.

Run the code:
To run the script, use the following command from terminal:

    python extract_contour.py <input_file.vti> <isovalue>

Example:

    python extract_contour.py Isabel_2D.vti -100

This will create an output file named `isocontour_output.vtp` in the same directory.

Output:
-------
- The extracted isocontour is saved in VTK PolyData format (.vtp)
- This can be visualized in ParaView

Notes:
------
- Do not use VTK's contour filter. This script uses a manually implemented algorithm.
- The dataset used is a pressure slice from the Hurricane Isabel simulation.

Author:
-------
Durba Smriti Saha

Course: CS661 - Visualization
