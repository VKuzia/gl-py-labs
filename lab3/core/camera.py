from moderngl_window.scene.camera import KeyboardCamera


class MovingCamera(KeyboardCamera):

    def __init__(self, keys):
        super().__init__(keys, fov=60.0, near=1, far=10)
        self.keys = keys
        self.velocity = 1.0
        self.mouse_sensitivity = 0.1
        self.set_position(0, 0, 5)

