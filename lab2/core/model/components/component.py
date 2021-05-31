from pyrr import Matrix44


class Component:

    def __init__(self, translation, rotation, geometry):
        self.translation = translation
        self.rotation = rotation
        self.geometry = geometry

    def model_view(self):
        rotation = Matrix44.from_eulers(self.rotation, dtype='f4')
        translation = Matrix44.from_translation(self.translation, dtype='f4')
        return translation * rotation
