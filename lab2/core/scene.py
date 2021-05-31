import moderngl
import typing as tp

from moderngl_window.opengl.vao import VAO
from pyrr import Matrix44

vertex_shader = '''
#version 330

in vec3 in_position;
in vec3 in_normal;
in vec2 in_texcoord_0;

uniform mat4 model;
uniform mat4 view;
uniform mat4 proj;

out vec2 uv;

void main() {
    gl_Position = proj * view * model * vec4(in_position, 1.0);
    uv = in_texcoord_0;
}
'''

fragment_shader = '''
#version 330

uniform sampler2D image;
in vec2 uv;
out vec4 out_color;

void main() {
    out_color = texture(image, uv);
}
'''


class Scene:

    def __init__(self, context: moderngl.Context, aspect_ratio: float):
        self.program = context.program(vertex_shader=vertex_shader, fragment_shader=fragment_shader)
        view_translation = (0, 0, -5.0)
        self.program['view'].write(Matrix44.from_translation(view_translation, dtype='f4'))
        self.update_proj(aspect_ratio)

    def update_proj(self, aspect_ratio: float):
        perspective_projection = Matrix44.perspective_projection(30, aspect_ratio, 1, 10, dtype='f4')
        self.program['proj'].write(perspective_projection)

    def render(self, rendering_data: tp.Tuple[VAO, Matrix44]):
        for geometry, model in rendering_data:
            self.program['model'].write(model)
            geometry.render(self.program)
