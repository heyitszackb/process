import pyxel
from Model.main import Model
from View.main import View

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()

    def run(self):
        pyxel.run(self.update, self.draw)

    def update(self):
            self.handle_input()
            self.model.update()

    def handle_input(self):
        if pyxel.btnp(pyxel.KEY_RIGHT):
            pass
        if pyxel.btnp(pyxel.KEY_LEFT):
            pass

    def draw(self): # executed each frame
        self.view.render(self.model) # executed each frame