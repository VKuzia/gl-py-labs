import moderngl_window as mglw
from pathlib import Path
import moderngl
from moderngl_window.scene import KeyboardCamera
from pyrr import Matrix44

from lab3.core.Camera import MovingCamera
from lab3.core.model.model import Model
from lab3.core.scene import Scene

texture_names = ["olga.png"]


class Window(mglw.WindowConfig):
    resource_dir = Path(__file__).parent.resolve() / 'resources'
    title = "Camera"
    aspect_ratio = 16 / 9

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.textures = [self.load_texture_2d(path) for path in texture_names]
        self.ctx.viewport = (0, 0, 720 * self.wnd.aspect_ratio, 720)
        self.ctx.enable_only(moderngl.CULL_FACE | moderngl.DEPTH_TEST)
        self.camera = MovingCamera(self.wnd.keys)
        self.model = Model(self.textures)
        self.scene = Scene(self.ctx, self.aspect_ratio, (0, 0, -5))

    def key_event(self, key, action, modifiers):
        self.camera.key_input(key, action, modifiers)

    def mouse_position_event(self, x: int, y: int, dx, dy):
        self.camera.rot_state(-dx, -dy)

    def render(self, time: float, interval: float):
        self.model.update(time, interval)
        self.scene.update_view(self.camera.matrix)
        self.scene.render(self.model.get_rendering_data())

    def resize(self, width: int, height: int):
        self.ctx.viewport = (0, 0, width, height)
        self.scene.update_proj(self.wnd.aspect_ratio)
