from solid import *
from solid.utils import *
from math import sin, cos, pi

OUTPUT_FILE_NAME = 'gimbal_base.scad'

BASE_THICKNESS = 6.2
BASE_WIDTH = 60
ATTACHMENT_WIDTH = 39.5
RAY_LENGTH = 120
RAY_WIDTH = 15
RAY_THICKNESS = BASE_THICKNESS
NUT_HOLE_THICKNESS = 2
NUT_HOLE_WIDTH = 5.3
MOUNTINH_HOLE_DIAMETER = 3.2
CORNER_SUPPORT_ANGLE = 45

res = union()

square_base = cube([BASE_WIDTH, BASE_WIDTH, BASE_THICKNESS], center=True)

mounting_holes = union()
nut_holes = union()
corner_supports = union()

rays = union()

mounting_hole = cylinder(d=MOUNTINH_HOLE_DIAMETER, h=(BASE_THICKNESS + 0.1), center=True)
nut_hole = cube([NUT_HOLE_WIDTH, NUT_HOLE_WIDTH, NUT_HOLE_THICKNESS], center=True)

for i in [(-ATTACHMENT_WIDTH / 2) + 4.3, (ATTACHMENT_WIDTH / 2) - 4.3]:
    for j in [(-ATTACHMENT_WIDTH / 2) + 4.3, (ATTACHMENT_WIDTH / 2) - 4.3]:
        mounting_holes += translate([i, j, 0])(mounting_hole)
        nut_holes += translate([i, j, -(BASE_THICKNESS / 2) + (NUT_HOLE_THICKNESS / 2)])(nut_hole)

for i in range(0, 360, 45):
    rays += rotate([0, 0, i])(cube([RAY_LENGTH, RAY_WIDTH, RAY_THICKNESS], center=True))
    corner_supports += translate([cos(i * pi / 180) * (RAY_LENGTH / 1.52), sin(i * pi / 180) * (RAY_LENGTH / 1.52), -(RAY_LENGTH / 5.91)])(
        rotate([0, CORNER_SUPPORT_ANGLE, i])(
            cube([RAY_LENGTH / 2, RAY_WIDTH, BASE_THICKNESS], center=True)
        )
    )

leveler = translate([0, 0, -63])(
    cube([300, 300, 50], center=True)
)

res += rays
res += square_base
res -= mounting_holes
res -= nut_holes
res += corner_supports
res -= leveler

scad_render_to_file(res, OUTPUT_FILE_NAME, file_header='$fa = 1;\n$fs = 0.1;')