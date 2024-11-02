from solid import *
from solid.utils import *
from math import sin, cos, pi

OUTPUT_FILE_NAME = 'gimbal_base.scad'

BASE_THICKNESS = 4
BASE_WIDTH = 60
ATTACHMENT_WIDTH = 39.5
RAY_LENGTH = 90
RAY_WIDTH = 30
RAY_THICKNESS = BASE_THICKNESS

res = union()

square_base = cube([BASE_WIDTH, BASE_WIDTH, BASE_THICKNESS], center=True)

mounting_holes = union()

rays = union()

mounting_hole = cylinder(d=3, h=(BASE_THICKNESS + 0.1), center=True)

for i in [(-ATTACHMENT_WIDTH / 2) + 4.3, (ATTACHMENT_WIDTH / 2) - 4.3]:
    for j in [(-ATTACHMENT_WIDTH / 2) + 4.3, (ATTACHMENT_WIDTH / 2) - 4.3]:
        mounting_holes += translate([i, j, 0])(mounting_hole)

for i in [(-BASE_WIDTH / 2) - (RAY_LENGTH / 2), (BASE_WIDTH / 2) + (RAY_LENGTH / 2)]:
        rays += translate([i, 0, 0])(cube([RAY_LENGTH, RAY_WIDTH, RAY_THICKNESS], center=True))

for i in [(-BASE_WIDTH / 2) - (RAY_LENGTH / 2), (BASE_WIDTH / 2) + (RAY_LENGTH / 2)]:
        rays += translate([0, i, 0])(cube([RAY_WIDTH, RAY_LENGTH, RAY_THICKNESS], center=True))

res += square_base - mounting_holes
res += rays

scad_render_to_file(res, OUTPUT_FILE_NAME, file_header='$fa = 1;\n$fs = 0.1;')