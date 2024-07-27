import pyxel

from Model.main import *

class View:
    def __init__(self):
        pyxel.init(100, 100, fps=100)
        pyxel.load("../joy.pyxres")
        pyxel.mouse(visible=True)

    # For future animation
    def update(self):
        pass

    def render(self, model: Model):
        pyxel.cls(7)

        mesh: NodeMesh = model.get_mesh()

        for node in mesh.get_nodes():
            pyxel.rect(node.x, node.y, 10,10,0)