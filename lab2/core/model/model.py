from lab2.core.model.components.cube import Cube


class Model:

    def __init__(self, textures):
        self.cubes = [Cube(textures[0], (-1.2, 0, -1), (0.5, 0.5, 0.5), 0.6),
                      Cube(textures[0], (0, 0, -1.5), (0, 0, 1), 1.0),
                      Cube(textures[0], (1.2, 0, -1), (1, 0, 0.5), 0.6)]
        self.components = [self.cubes]

    def update(self, time, interval):
        for cube in self.cubes:
            cube.update(time, interval)

    def get_rendering_data(self):
        return [(cube.geometry, cube.model_view()) for cube in self.cubes]
