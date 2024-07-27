from typing import List
import copy
import random
from .drag_manager import DragManager
from .node import Node
from .node_mesh import NodeMesh
from .click_manager import ClickManager

class Model:
    def __init__(self) -> None:
        n0 = Node(0)
        n1 = Node(1)
        n2 = Node(2)

        n0.add_connection(n1)
        n1.add_connection(n2)

        self.node_mesh = NodeMesh([n0, n1, n2])
        self.drag_manager = DragManager()
        self.click_manager = ClickManager()
    def update(self) -> None:
        pass

    def get_mesh(self) -> NodeMesh:
        return self.node_mesh
    
    def step(self) -> None:
        self.node_mesh.step()
    
    def get_nodes(self) -> List[Node]:
        return self.node_mesh.get_nodes()

    def add_new_node(self) -> None:
        self.node_mesh.add_new_node()
    
    def handle_drag(self, mouse_x: int, mouse_y: int, is_mouse_down: bool) -> None:
        self.drag_manager.handle_drag(mouse_x, mouse_y, is_mouse_down, self.get_nodes())
    
    def handle_click(self, mouse_x: int, mouse_y: int) -> None:
        self.click_manager.handle_click(mouse_x, mouse_y, self.get_nodes())