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

front_rear_axels = union()

for i in [-AXEL_HORIZONTAL_OFFSET, AXEL_HORIZONTAL_OFFSET]:
    axel_base = rotate([90, 0, 0])(
        cylinder(r=AXEL_RADIUS, h=AXEL_LENGTH, center=True)
    )

    cutting_cubes = union()
    wheel_bays = union()

    wheels = union()

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

        bold_tire = rotate_extrude(360)(
            polygon(points=[[-WHEEL_INNER_RADIUS, -WHEEL_MIN_WIDTH/2], [-WHEEL_INNER_RADIUS, WHEEL_MIN_WIDTH/2], [-WHEEL_OUTER_RADIUS, WHEEL_MAX_WIDTH/2], [-WHEEL_OUTER_RADIUS, -WHEEL_MAX_WIDTH/2]])
        )

        tire = bold_tire

        for protector_angle in range(0, 360, 12):
            dx = WHEEL_OUTER_RADIUS * cos(protector_angle * pi / 180)
            dy = WHEEL_OUTER_RADIUS * sin(protector_angle * pi / 180)
            tire -= translate([dx, dy, 0])(
                rotate([0, 0, protector_angle])(
                    cube([1, 1, WHEEL_MAX_WIDTH], center=True)
                )
            )

        rim = rotate_extrude(360)(
            translate([WHEEL_INNER_RADIUS, 0])(
                square([1, WHEEL_MIN_WIDTH], center=True)
            )
        )

        wheels += translate([0, j * ((AXEL_LENGTH / 2) + 30), 0])(
            union()(
                tire,
                rim
            )
        )

    axel_base -= cutting_cubes
    axel_base -= wheel_bays

    axel_base += wheels

    front_rear_axels += translate([i, 0, 0])(
        axel_base
    )

center_axel = rotate([0, 90, 0])(
    cylinder(r=AXEL_RADIUS, h=(2 * (AXEL_HORIZONTAL_OFFSET + 0.1)), center=True)
)

res = front_rear_axels + center_axel

scad_render_to_file(res, OUTPUT_FILE_NAME, file_header='$fa = 1;\n$fs = 0.1;')
