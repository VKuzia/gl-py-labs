from pathlib import Path
from pyrr import Matrix44

import moderngl
import moderngl_window
from lab2.utils.window import CameraWindow


class CubeModel(CameraWindow):
    aspect_ratio = 16 / 9
    resource_dir = Path(__file__).parent.resolve() / 'resources'
    title = "Cube Model"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.wnd.mouse_exclusivity = True

        self.scene = self.load_scene('scenes/crate.obj')

        self.camera.projection.update(near=0.1, far=100.0)
        self.camera.velocity = 7.0
        self.camera.mouse_sensitivity = 0.3

    def render(self, time: float, frametime: float):
        self.ctx.enable_only(moderngl.DEPTH_TEST | moderngl.CULL_FACE)

        translation = Matrix44.from_translation((0, 0, -1.5))
        rotation = Matrix44.from_eulers((0, 0, 0))
        model_matrix = translation * rotation
        camera_matrix = self.camera.matrix * model_matrix

        self.scene.draw(
            projection_matrix=self.camera.projection.matrix,
            camera_matrix=camera_matrix,
            time=time,
        )


if __name__ == '__main__':
    moderngl_window.run_window_config(CubeModel)