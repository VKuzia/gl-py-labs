from moderngl import Program
from pyrr import Matrix44

from lab2.core.cube import Cube
from lab2.core.model import Model


class Scene:

    def __init__(self):
        self.view_translation = (0, 0, -5.0)

    def render(self, program: Program, model: Model):
        for item in model.cubes:
            program['model'].write(item.model_view())
            item.geometry.render(program)
