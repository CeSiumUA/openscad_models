from solid import *
from solid.utils import *
from math import sin, cos, pi

OUTPUT_FILE_NAME = 'cart.scad'
AXEL_HORIZONTAL_OFFSET = 30
AXEL_RADIUS = 5
WHEEL_INNER_RADIUS = AXEL_RADIUS + 0.35
AXEL_LENGTH = 60
WHEEL_MIN_WIDTH = 4
WHEEL_MAX_WIDTH = 8
WHEEL_OUTER_RADIUS = 10

res = union()

res += sphere(100, segments=420)

# scad_render_to_file(res, 'test.scad', file_header='$fa = 1;\n$fs = 0.1;')
scad_render_to_file(res, 'test.scad')