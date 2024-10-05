from solid import *
from solid.utils import *

res = union()(
    cube([15, 5, 2.5], center=True),
    translate([1.25, 0, 2.5 - 0.001])(cube([7.5, 5, 2.5], center=True)),
    translate([-5, -3.75, 0])(
        rotate([90, 0, 0])(
            cylinder(h=0.75, r=2, center=True)
        )
    ),
    translate([-5, 3.75, 0])(
        rotate([90, 0, 0])(
            cylinder(h=0.75, r=2, center=True)
        )
    ),
    translate([5, -3.75, 0])(
        rotate([90, 0, 0])(
            cylinder(h=0.75, r=2, center=True)
        )
    ),
    translate([5, 3.75, 0])(
        rotate([90, 0, 0])(
            cylinder(h=0.75, r=2, center=True)
        )
    ),
    translate([-5, 0, 0])(
        rotate([90, 0, 0])(
            cylinder(h=7.5, r=0.5, center=True)
        )
    ),
    translate([5, 0, 0])(
        rotate([90, 0, 0])(
            cylinder(h=7.5, r=0.5, center=True)
        )
    )
)

scad_render_to_file(res, 'cube.scad')