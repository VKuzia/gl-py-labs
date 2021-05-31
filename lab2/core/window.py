import moderngl_window as mglw
from moderngl_window.scene.camera import Camera
from pathlib import Path
from pyrr import Matrix44
import moderngl
from moderngl_window import geometry

from lab2.core.model import Model
from lab2.core.scene import Scene

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

texture_names = ["olga.png", "olga.png", "olga.png"]


class Window(mglw.WindowConfig):
    resource_dir = Path(__file__).parent.resolve() / 'resources'
    title = "Cube Model"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.textures = [self.load_texture_2d(path) for path in texture_names]
        self.program = self.ctx.program(vertex_shader=vertex_shader, fragment_shader=fragment_shader)
        self.program['view'].write(Matrix44.from_translation((0, 0, -5.0), dtype='f4'))
        self.program['proj'].write(Matrix44.perspective_projection(30, 16 / 9, 1, 10, dtype='f4'))
        self.model = Model(self.textures)
        self.scene = Scene()

    def render(self, time: float, frametime: float):
        self.ctx.enable_only(moderngl.CULL_FACE | moderngl.DEPTH_TEST)
        self.model.update(frametime)
        self.scene.render(self.program, self.model)

    def resize(self, width: int, height: int):
        pass
