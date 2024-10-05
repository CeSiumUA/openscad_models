from solid import *
from solid.utils import *

OUTPUT_FILE_NAME = 'wheelset.scad'
AXEL_HORIZONTAL_OFFSET = 30
AXEL_RADIUS = 5
WHEEL_INNER_RADIUS = AXEL_RADIUS + 0.1
AXEL_LENGTH = 60
WHEEL_MIN_WIDTH = 4
WHEEL_MAX_WIDTH = 8
WHEEL_OUTER_RADIOS = 10

res = union()

for i in [-AXEL_HORIZONTAL_OFFSET, AXEL_HORIZONTAL_OFFSET]:
    direction_wheelset = union()
    for j in [-1, 1]:

        tire = rotate([90, 0, 0])(
            rotate_extrude(360)(
                polygon(points=[[-WHEEL_INNER_RADIUS, -WHEEL_MIN_WIDTH/2], [-WHEEL_INNER_RADIUS, WHEEL_MIN_WIDTH/2], [-WHEEL_OUTER_RADIOS, WHEEL_MAX_WIDTH/2], [-WHEEL_OUTER_RADIOS, -WHEEL_MAX_WIDTH/2]])
            )
        )

        rim = rotate([90, 0, 0])(
            rotate_extrude(360)(
                translate([WHEEL_INNER_RADIUS, 0])(
                    square([1, WHEEL_MIN_WIDTH], center=True)
                )
            )
        )

        direction_wheelset += translate([0, j * ((AXEL_LENGTH / 2) - 4), 0])(
            union()(
                tire,
                rim
            )
        )

    res += translate([i, 0, 0])(
        direction_wheelset
    )

scad_render_to_file(res, OUTPUT_FILE_NAME, file_header='$fa = 1;\n$fs = 0.1;')