import pyxel
from Model.main import Model
from View.main import View

class Controller:
    def __init__(self) -> None:
        self.model = Model()
        self.view = View()

    def run(self) -> None:
        pyxel.run(self.update, self.draw)

    def update(self) -> None:
        self.handle_input()
        self.model.update()

    def handle_input(self) -> None:
        mouse_x, mouse_y = pyxel.mouse_x, pyxel.mouse_y
        is_mouse_down = pyxel.btn(pyxel.MOUSE_BUTTON_LEFT)
        is_mouse_clicked = pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT)



        self.model.handle_drag(mouse_x, mouse_y, is_mouse_down)
        if is_mouse_clicked:
            self.model.handle_click(mouse_x, mouse_y)

        if pyxel.btnp(pyxel.KEY_RIGHT):
            self.model.step()
        if pyxel.btnp(pyxel.KEY_RETURN):
            self.model.add_new_node()

    def draw(self) -> None:
        self.view.render(self.model)