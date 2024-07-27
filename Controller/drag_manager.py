from Model.main import *
from typing import Union
import math

class DragManager:
    def __init__(self, model: Model):
        self.model: Model = model
        self.dragging: bool = False
        self.drag_offset_x: int = 0
        self.drag_offset_y: int = 0
        self.dragged_node: Union[int, None] = None

    def handle_drag(self, mouse_x: int, mouse_y: int, is_mouse_down: bool):
        if is_mouse_down:
            if not self.dragging:
                self.start_drag(mouse_x, mouse_y)
            else:
                self.continue_drag(mouse_x, mouse_y)
        else:
            if self.dragging:
                self.end_drag()

    def start_drag(self, mouse_x: int, mouse_y: int):
        self.dragging = False
        self.dragged_node = None
        for node in self.model.get_nodes():
            if self.is_mouse_over_node(mouse_x, mouse_y, node):
                self.dragging = True
                self.dragged_node = node
                self.drag_offset_x = node.x - mouse_x
                self.drag_offset_y = node.y - mouse_y
                break  # Only drag the first node we find

    def continue_drag(self, mouse_x: int, mouse_y: int):
        if self.dragging and self.dragged_node:
            self.dragged_node.x = mouse_x + self.drag_offset_x
            self.dragged_node.y = mouse_y + self.drag_offset_y

    def end_drag(self):
        self.dragging = False
        self.dragged_node = None

    @staticmethod
    def is_mouse_over_node(mouse_x: int, mouse_y: int, node: 'Node') -> bool:
        # Calculate the distance between the mouse and the center of the node
        distance = math.sqrt((mouse_x - node.x)**2 + (mouse_y - node.y)**2)
        # Check if the distance is less than or equal to the radius
        return distance <= node.size