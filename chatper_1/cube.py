from solid import *
from solid.utils import *

res = union()(
    cube([50, 20, 10], center=True),
    translate([5, 0, 10 - 0.001])(cube([30, 20, 10], center=True)),
    translate([-20, -15, 0])(
        rotate([90, 0, 0])(
            cylinder(h=3, r=8, center=True)
        )
    ),
    translate([-20, 15, 0])(
        rotate([90, 0, 0])(
            cylinder(h=3, r=8, center=True)
        )
    ),
    translate([20, -15, 0])(
        rotate([90, 0, 0])(
            cylinder(h=3, r=8, center=True)
        )
    ),
    translate([20, 15, 0])(
        rotate([90, 0, 0])(
            cylinder(h=3, r=8, center=True)
        )
    ),
    translate([-20, 0, 0])(
        rotate([90, 0, 0])(
            cylinder(h=30, r=2, center=True)
        )
    ),
    translate([20, 0, 0])(
        rotate([90, 0, 0])(
            cylinder(h=30, r=2, center=True)
        )
    )
)

scad_render_to_file(res, 'cube.scad', file_header='$fa = 1;$fs = 0.1;')