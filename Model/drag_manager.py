from Model.main import *
from typing import Union, List
import math
from .node import Node

class DragManager:
    def __init__(self):
        self.dragging: bool = False
        self.drag_offset_x: int = 0
        self.drag_offset_y: int = 0
        self.dragged_node: Union[int, None] = None

    def handle_drag(self, mouse_x: int, mouse_y: int, is_mouse_down: bool, nodes: List[Node]) -> None:
        if is_mouse_down:
            if not self.dragging:
                self.start_drag(mouse_x, mouse_y, nodes)
            else:
                self.continue_drag(mouse_x, mouse_y)
        else:
            if self.dragging:
                self.end_drag()

    def start_drag(self, mouse_x: int, mouse_y: int, nodes: List[Node]) -> None:
        self.dragging = False
        self.dragged_node = None
        for node in nodes:
            if node.is_mouse_over(mouse_x, mouse_y):
                self.dragging = True
                self.dragged_node = node
                self.drag_offset_x = node.x - mouse_x
                self.drag_offset_y = node.y - mouse_y
                break  # Only drag the first node we find

    def continue_drag(self, mouse_x: int, mouse_y: int) -> None:
        if self.dragging and self.dragged_node:
            self.dragged_node.x = mouse_x + self.drag_offset_x
            self.dragged_node.y = mouse_y + self.drag_offset_y

    def end_drag(self) -> None:
        self.dragging = False
        self.dragged_node = None