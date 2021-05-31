import moderngl_window as mglw
from moderngl_window.geometry import cube
from pyrr import Matrix44


class Cube:
    def __init__(self, texture, translation, rotation, size):
        self.texture = texture
        self.geometry = cube(size=(size, size, size))
        self.translation = translation
        self.rotation = rotation
        self.texture.use(location=0)

    def model_view(self):
        rotation = Matrix44.from_eulers(self.rotation, dtype='f4')
        translation = Matrix44.from_translation(self.translation, dtype='f4')
        return translation * rotation
