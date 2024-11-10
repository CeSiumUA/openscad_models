from solid import *
from solid.utils import *
from math import sin, cos, pi

OUTPUT_FILE_NAME = 'log_antenna_case.scad'
ANTENNA_LENGTH = 444.5
ANTENNA_BEGIN_WIDTH = 250
ANTENNA_END_WIDTH = 70
ANTENNA_THICKNESS = 15

CUTTING_CASE_SCALING = 0.95

res = union()

base_trapezoid = polygon(points=[
    [ANTENNA_BEGIN_WIDTH / 2, 0],
    [ANTENNA_END_WIDTH / 2, ANTENNA_LENGTH],
    [-ANTENNA_END_WIDTH / 2, ANTENNA_LENGTH],
    [-ANTENNA_BEGIN_WIDTH / 2, 0]
])

base_case = linear_extrude(height=ANTENNA_THICKNESS)(base_trapezoid) + translate([0, ANTENNA_LENGTH - 2, 0])(
    cylinder(d = ANTENNA_END_WIDTH, h = ANTENNA_THICKNESS)
)

cutting_case = scale([CUTTING_CASE_SCALING, CUTTING_CASE_SCALING, 1])(
    translate([0, (ANTENNA_LENGTH / 2) - (CUTTING_CASE_SCALING * (ANTENNA_LENGTH / 2)), 5])(
        base_case
    )
)

base_case -= cutting_case

res += base_case

scad_render_to_file(res, OUTPUT_FILE_NAME, file_header='$fa = 1;\n$fs = 0.1;')