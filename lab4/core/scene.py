import moderngl
import typing as tp

from moderngl_window.opengl.vao import VAO
from pyrr import Matrix44

vertex_shader = '''

'''

fragment_shader = '''
#version 330

'''


class Scene:

    def __init__(self, program: moderngl.Program, aspect_ratio: float, camera_translation):
        self.program = program
        self.camera_translation_matrix = Matrix44.from_translation(camera_translation, dtype='f4')
        self.update_view(self.camera_translation_matrix)
        self.update_proj(aspect_ratio)

    def update_proj(self, aspect_ratio: float):
        perspective_projection = Matrix44.perspective_projection(30, aspect_ratio, 1, 10, dtype='f4')
        self.program['proj'].write(perspective_projection)

    def update_view(self, camera_matrix):
        self.program['view'].write(camera_matrix)

    def render(self, rendering_data: tp.Tuple[VAO, Matrix44]):
        for geometry, model in rendering_data:
            self.program['model'].write(model)
            geometry.render(self.program)
