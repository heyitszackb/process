from math import atan2, cos, sin, pi, sqrt
import pyxel
from Model.main import Node

def draw_arrow(node1: Node, node2: Node, color: int):
    # Calculate the angle of the line
    angle = atan2(node2.y - node1.y, node2.x - node1.x)

    # Calculate the start point of the arrow (end of the line)
    x2_adj = node2.x - node2.size * cos(angle)
    y2_adj = node2.y - node2.size * sin(angle)

    # Draw the line
    pyxel.line(node1.x, node1.y, x2_adj, y2_adj, color)

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