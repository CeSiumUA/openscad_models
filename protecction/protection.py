from solid import *
from solid.utils import *
from math import sin, cos, pi

OUTPUT_FILE_NAME = 'protection.scad'

res = union()

main_cube = cube([150, 30, 50], center=True)

cutting_cube = union()

cutting_cube1 = rotate([0, 18, 0])(
    translate([0, 0, 25])(
        cube([300, 150, 50], center=True)
    )
)

cutting_cube += cutting_cube1

main_cube -= cutting_cube

res += main_cube

scad_render_to_file(res, OUTPUT_FILE_NAME, file_header='$fa = 1;\n$fs = 0.1;')