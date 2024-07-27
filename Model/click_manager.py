# click_manager.py
from typing import List
from .node import Node
import pyxel

class ClickManager:
    def __init__(self):
        self.last_click_time = 0
        self.last_clicked_node = None
        self.double_click_threshold = 20  # Assuming 30 FPS, this is about 0.5 seconds
        self.is_in_connecting_mode = False

    def handle_click(self, mouse_x: int, mouse_y: int, nodes: List[Node]) -> None:
        clicked_node = self.get_node_at(mouse_x, mouse_y, nodes)
        
        if self.is_in_connecting_mode:
            self.handle_connecting_click(clicked_node, nodes)
        else:
            self.handle_selection_click(clicked_node, nodes)

    def handle_selection_click(self, clicked_node: Node, nodes: List[Node]) -> None:
        self.reset_node_selections(nodes)
        
        if clicked_node:
            if self.is_double_click(clicked_node):
                self.start_connecting_mode(clicked_node)
            else:
                self.update_last_click_info(clicked_node)

    def handle_connecting_click(self, clicked_node: Node, nodes: List[Node]) -> None:
        if clicked_node and (clicked_node != self.last_clicked_node):
            self.create_connection(clicked_node)
        
        self.exit_connecting_mode(nodes)

    def is_double_click(self, clicked_node: Node) -> bool:
        current_time = pyxel.frame_count
        return (clicked_node == self.last_clicked_node and 
                current_time - self.last_click_time < self.double_click_threshold)

    def start_connecting_mode(self, clicked_node: Node) -> None:
        clicked_node.is_selected = True
        self.is_in_connecting_mode = True
        print(f"Started connecting mode from node: {clicked_node.data}")

    def update_last_click_info(self, clicked_node: Node) -> None:
        self.last_click_time = pyxel.frame_count
        self.last_clicked_node = clicked_node
        print(f"Selected node: {clicked_node.data}")

    def create_connection(self, clicked_node: Node) -> None:
        self.last_clicked_node.manage_connection_request(clicked_node)
        print(f"Connected {self.last_clicked_node.data} to {clicked_node.data}")

    def exit_connecting_mode(self, nodes: List[Node]) -> None:
        self.reset_node_selections(nodes)
        self.is_in_connecting_mode = False
        print("Exited connecting mode")

    def reset_node_selections(self, nodes: List[Node]) -> None:
        for node in nodes:
            node.is_selected = False

    def get_node_at(self, x: int, y: int, nodes: List[Node]) -> Node:
        for node in nodes:
            if node.is_mouse_over(x, y):
                return node
        return None