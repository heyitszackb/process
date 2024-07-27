import pyxel
from math import atan2, cos, sin, pi, sqrt
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

        mesh = model.get_mesh()
        
        # Render Node Connections with Arrows
        for node in mesh.get_nodes():
            for connected_node in node.connections:
                self.draw_arrow(node.x, node.y, connected_node.x, connected_node.y, node.size, 0)
        
        # Render nodes
        for node in mesh.get_nodes():
            pyxel.circ(node.x, node.y, node.size, 0)
            pyxel.text(node.x, node.y, str(node.data), 7)
        

    def draw_arrow(self, x1, y1, x2, y2, radius, color):
        # Calculate the angle of the line
        angle = atan2(y2 - y1, x2 - x1)

        # Calculate the start point of the arrow (end of the line)
        x2_adj = x2 - radius * cos(angle)
        y2_adj = y2 - radius * sin(angle)

        # Draw the line
        pyxel.line(x1, y1, x2_adj, y2_adj, color)

        # Length of the arrowhead lines
        arrow_length = 5
        arrow_angle = pi / 6  # 30 degrees

        # Calculate the end points of the arrowhead lines
        x3 = x2_adj - arrow_length * cos(angle - arrow_angle)
        y3 = y2_adj - arrow_length * sin(angle - arrow_angle)
        x4 = x2_adj - arrow_length * cos(angle + arrow_angle)
        y4 = y2_adj - arrow_length * sin(angle + arrow_angle)

        # Draw the arrowhead
        pyxel.tri(x2_adj, y2_adj, x3, y3, x4, y4, color)