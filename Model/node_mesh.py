from typing import List
from .node import Node

class NodeMesh:
    def __init__(self, nodes: List[Node] = []) -> None:
        self.nodes: List[Node] = nodes
    
    def add_node(self, node: Node) -> None:
        self.nodes.append(node)
    
    def conect_to(self, node1: Node,node2: Node) -> None:
        node1.add_connection(node2)
    
    def add_new_node(self) -> None:
        n = Node(0)
        self.add_node(n)
    
    def step(self) -> None:
        for node in self.nodes:
            node.send()
        
        for node in self.nodes:
            node.process()
    
    def get_nodes(self) -> List[Node]:
        return self.nodes
    
    def __repr__(self) -> str:
        node_data: List[int] = [node.data for node in self.nodes]
        return str(node_data)