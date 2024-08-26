import random
import math

import mathutils
import bpy

CAMERA_LOCATION_RANGE = (15, 20)
# CAMERA_LOCATION = (0, 20, 2) # eye level-ish, 10 ft away
CAMERA_ROTATION = (-1.47, 0, 0)
LIGHT_LOCATION = (0, 0, 4) # top left

ROTATION_RANGE = (0, math.pi * 2)
SCALE_RANGE = (1., 1.)
LOCATION_RANGE_X = (-3, 3)
LOCATION_RANGE_Y = (-3, 3)
LOCATION_RANGE_Z = (-2, 2)
R1_RANGE = (.1, 1.)
R2_RANGE = (.1, 1.)
SIZE_RANGE = (.1, 1.)
N_OBJECTS = 10

# create new empty scene
bpy.ops.scene.new(type='EMPTY')

# create camera
camera_data = bpy.data.cameras.new(name='camera')
camera_data.lens = 55
camera = bpy.data.objects.new(name='camera', object_data=camera_data)
bpy.context.collection.objects.link(camera)

camera.location = (12, 12, 2)
camera.rotation_euler = mathutils.Euler((1.45, 0, 2.35))
# camera.rotation_euler = mathutils.Euler(CAMERA_ROTATION)

# create objects
types = ['cube', 'cone', 'cylinder', 'sphere']
for i in range(N_OBJECTS):
    obj_type = random.choice(types)
    location = (
        random.uniform(*LOCATION_RANGE_X),
        random.uniform(*LOCATION_RANGE_Y),
        random.uniform(*LOCATION_RANGE_Z),
    )
    rotation = mathutils.Euler(
        [random.uniform(*ROTATION_RANGE) for i in range(3)]
    )
    scale = [random.uniform(*SCALE_RANGE) for i in range(3)]

    if obj_type == 'cube':
        size = [random.uniform(*SIZE_RANGE)] * 3
        bpy.ops.mesh.primitive_cube_add(location=location, rotation=rotation, scale=scale)
    elif obj_type == 'cone':
        radius = random.uniform(*R1_RANGE)
        depth = random.uniform(*SIZE_RANGE)
        bpy.ops.mesh.primitive_cone_add(location=location, rotation=rotation, scale=scale, radius1=radius, radius2=0, depth=depth)
    elif obj_type == 'cylinder':
        radius = random.uniform(*R1_RANGE)
        depth = random.uniform(*SIZE_RANGE)
        bpy.ops.mesh.primitive_cylinder_add(location=location, rotation=rotation, scale=scale, radius=radius, depth=depth)
    elif obj_type == 'sphere':
        radius = random.uniform(*R1_RANGE)
        bpy.ops.mesh.primitive_uv_sphere_add(location=location, rotation=rotation, scale=scale, radius=radius)
    else:
        raise RuntimeError('invalid type')
