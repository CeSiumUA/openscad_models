from solid import *
from solid.utils import *

OUTPUT_FILE_NAME = 'cart.scad'
AXEL_HORIZONTAL_OFFSET = 30
AXEL_RADIUS = 5
AXEL_LENGTH = 60

front_rear_axels = union()

for i in [-AXEL_HORIZONTAL_OFFSET, AXEL_HORIZONTAL_OFFSET]:
    axel_base = rotate([90, 0, 0])(
        cylinder(r=AXEL_RADIUS, h=AXEL_LENGTH, center=True)
    )

    cutting_cubes = union()
    wheel_bays = union()

    for j in [-1, 1]:
        cutting_cubes += translate([0, j * ((AXEL_LENGTH / 2) - 2.5), 0])(
            cube([20, 10, 2.5], center=True)
        )
        wheel_bays += translate([0, j * ((AXEL_LENGTH / 2) - 4), 0])(
            rotate([90, 0, 0])(
                rotate_extrude(360)(
                    translate([AXEL_RADIUS, 0])(
                        square([1, 4], center=True)
                    )
                )
            )
        )

    axel_base -= cutting_cubes
    axel_base -= wheel_bays

    front_rear_axels += translate([i, 0, 0])(
        axel_base
    )

center_axel = rotate([0, 90, 0])(
    cylinder(r=AXEL_RADIUS, h=(2 * (AXEL_HORIZONTAL_OFFSET + 0.1)), center=True)
)

res = front_rear_axels + center_axel

scad_render_to_file(res, 'cube.scad', file_header='$fa = 1;\n$fs = 0.1;')
