from moderngl import Texture
from moderngl_window.geometry import cube
import numpy as np
import typing as tp

from lab4.core.model.components.component import Component


def _update_rotation_cord(rotation_cord: float, time: float):
    result = rotation_cord + time * 1.0
    if result > 1.0:
        result -= 1.0
    return result


class Cube(Component):

    def __init__(self, texture: Texture, translation: tp.Tuple[float, float, float],
                 rotation: tp.Tuple[float, float, float], size: float):
        super().__init__(translation, rotation, cube(size=(size, size, size)))
        self.texture = texture
        self.base_translation = translation
        self.size = size
        self.texture.use(location=0)

    def update(self, time: float, interval: float):
        self.rotation = tuple([_update_rotation_cord(rotation_cord, interval) for rotation_cord in self.rotation])
        self.translation = (self.base_translation[0] + np.sin(time), self.base_translation[1] + np.cos(time),
                            self.base_translation[2] + (np.sin(time) + np.cos(time)) * self.size)
