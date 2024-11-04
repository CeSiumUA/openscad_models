from solid import *
from solid.utils import *
from math import sin, cos, pi

OUTPUT_FILE_NAME = 'gimbal_base.scad'

BASE_THICKNESS = 6.2
BASE_WIDTH = 60
ATTACHMENT_WIDTH = 39.5
RAY_LENGTH = 150
RAY_WIDTH = 15
RAY_THICKNESS = BASE_THICKNESS
NUT_HOLE_THICKNESS = 2
NUT_HOLE_WIDTH = 5.3
MOUNTINH_HOLE_DIAMETER = 3.2

res = union()

square_base = cube([BASE_WIDTH, BASE_WIDTH, BASE_THICKNESS], center=True)

mounting_holes = union()
nut_holes = union()

rays = union()

mounting_hole = cylinder(d=MOUNTINH_HOLE_DIAMETER, h=(BASE_THICKNESS + 0.1), center=True)
nut_hole = cube([NUT_HOLE_WIDTH, NUT_HOLE_WIDTH, NUT_HOLE_THICKNESS], center=True)

for i in [(-ATTACHMENT_WIDTH / 2) + 4.3, (ATTACHMENT_WIDTH / 2) - 4.3]:
    for j in [(-ATTACHMENT_WIDTH / 2) + 4.3, (ATTACHMENT_WIDTH / 2) - 4.3]:
        mounting_holes += translate([i, j, 0])(mounting_hole)
        nut_holes += translate([i, j, -(BASE_THICKNESS / 2) + (NUT_HOLE_THICKNESS / 2)])(nut_hole)

for i in range(0, 180, 45):
    rays += rotate([0, 0, i])(cube([RAY_LENGTH, RAY_WIDTH, RAY_THICKNESS], center=True))

res += rays
res += square_base
res -= mounting_holes
res -= nut_holes

scad_render_to_file(res, OUTPUT_FILE_NAME, file_header='$fa = 1;\n$fs = 0.1;')