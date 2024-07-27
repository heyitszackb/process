from math import atan2, cos, sin, pi, sqrt
import pyxel

def draw_arrow(x1: float, y1: float, x2: float, y2: float, color: int, node_size: float = 3):
    # Calculate the angle of the line
    angle = atan2(y2 - y1, x2 - x1)

    # Calculate the start point of the arrow (end of the line)
    x2_adj = x2 - node_size * cos(angle)
    y2_adj = y2 - node_size * sin(angle)

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