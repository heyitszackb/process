import pyxel
from Model.main import *
from .helpers import draw_arrow

class View:
    def __init__(self) -> None:
        pyxel.init(100, 100, fps=100)
        pyxel.load("../joy.pyxres")
        pyxel.mouse(visible=True)

    # For future animation
    def update(self) -> None:
        pass

    def render(self, model: Model) -> None:
        pyxel.cls(7)

        nodes = model.get_nodes()
        
        # Render Node Connections with Arrows
        for node in nodes:
            for connected_node in node.connections:
                draw_arrow(node, connected_node, 0)
        
        # Render nodes
        for node in nodes:
            pyxel.circ(node.x, node.y, node.size, 0)
            pyxel.text(node.x, node.y, str(node.data), 7)