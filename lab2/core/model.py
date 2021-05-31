from lab2.core.cube import Cube


def update_rotation_cord(rotation_cord, time):
    result = rotation_cord + time * 1.0
    if result > 1.0:
        result -= 1.0
    return result


def update_cube(cube, time):
    cube.rotation = tuple([update_rotation_cord(rotation_cord, time) for rotation_cord in cube.rotation])


class Model:

    def __init__(self, textures):
        self.cubes = [Cube(textures[i], ((i - 1) * 2, 0, -2), (0, 0, 0), (i + 1) / 2) for i in range(len(textures))]

    def update(self, time):
        for cube in self.cubes:
            update_cube(cube, time)
