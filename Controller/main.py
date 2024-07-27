import pyxel
from Model.main import Model
from View.main import View
from .drag_manager import DragManager

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()
        self.drag_manager = DragManager(self.model)

    def run(self):
        pyxel.run(self.update, self.draw)

    def update(self):
        self.handle_input()
        self.model.update()

    def handle_input(self):
        mouse_x, mouse_y = pyxel.mouse_x, pyxel.mouse_y
        is_mouse_down = pyxel.btn(pyxel.MOUSE_BUTTON_LEFT)
        self.drag_manager.handle_drag(mouse_x, mouse_y, is_mouse_down)

        if pyxel.btnp(pyxel.KEY_RETURN):
            self.model.step()

    def draw(self):
        self.view.render(self.model)