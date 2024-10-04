from solid import *
from solid.utils import *

left_cube = translate([-24, 0, 0])(
    union()(
        cube(15, center=True),
        sphere(10)
    )
)

center_cube = intersection()(
    cube(15, center=True),
    sphere(10)
)

right_cube = translate([24, 0, 0])(
    difference()(
        cube(15, center=True),
        sphere(10)
    )
)

res = left_cube + center_cube + right_cube

scad_render_to_file(res, 'csg.scad')