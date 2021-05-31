from moderngl import Texture

from lab3.core.model.components.cube import Cube
import typing as tp

from lab3.core.model.components.sphere import Sphere


class Model:

    def __init__(self, textures: tp.List[Texture]):
        self.cubes = [Cube(textures[0], (-1.2, 0, -1), (0.5, 0.5, 0.5), 0.6),
                      Cube(textures[0], (0, 0, -1.5), (0, 0, 1), 1.0),
                      Cube(textures[0], (1.2, 0, -1), (1, 0, 0.5), 0.6)]
        self.spheres = [Sphere(textures[0], (0, 0, 0), (0, 0, 0), 0.3)]
        self.components = [self.cubes, self.spheres]

    def update(self, time: float, interval: float):
        for cube in self.cubes:
            cube.update(time, interval)

    def get_rendering_data(self):
        return [(item.geometry, item.model_view()) for component_set in
                self.components for item in component_set]
