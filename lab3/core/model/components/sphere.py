from moderngl import Texture
import typing as tp

from moderngl_window.geometry import sphere

from lab3.core.model.components.component import Component


class Sphere(Component):

    def __init__(self, texture: Texture, translation: tp.Tuple[float, float, float],
                 rotation: tp.Tuple[float, float, float], size: float):
        super().__init__(translation, rotation, sphere(radius=size))
        self.texture = texture
        self.base_translation = translation
        self.size = size
        self.texture.use(location=0)