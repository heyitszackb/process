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

        # Render nodes
        for node in mesh.get_nodes():
            pyxel.circ(node.x, node.y, 5,0)
        
        # Render Node Connections
        for node in mesh.get_nodes():
            for connected_node in node.connections:
                pyxel.line(node.x, node.y, connected_node.x, connected_node.y,0)
