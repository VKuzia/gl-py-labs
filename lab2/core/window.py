import moderngl_window as mglw
from pathlib import Path
import moderngl

from lab2.core.model.model import Model
from lab2.core.scene import Scene

texture_names = ["olga.png"]


class Window(mglw.WindowConfig):
    resource_dir = Path(__file__).parent.resolve() / 'resources'
    title = "Cube Model"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.textures = [self.load_texture_2d(path) for path in texture_names]
        self.ctx.viewport = (0, 0, 1280, 720)
        self.model = Model(self.textures)
        self.scene = Scene(self.ctx)

    def render(self, time: float, interval: float):
        self.ctx.enable_only(moderngl.CULL_FACE | moderngl.DEPTH_TEST)
        self.model.update(time, interval)
        self.scene.render(self.model.get_rendering_data())

