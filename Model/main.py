from typing import List
import copy
import random

class Model:
    def __init__(self):
        n0 = Node(1)
        n1 = Node(0)
        n2 = Node(1)

        n0.add_connection(n1)
        n1.add_connection(n2)

        self.node_mesh = NodeMesh([n0, n1, n2])
    def update(self):
        pass

    def get_mesh(self):
        return self.node_mesh
    
    def step(self):
        self.node_mesh.step()
    
    def get_nodes(self):
        return self.node_mesh.get_nodes()


class Node:
    def __init__(self, data: int = 0):
        self.size = 6
        self.incoming_data: int = 0
        self.data: int = data
        self.connections: List[Node] = []
        self.x: int = random.randint(0,100)
        self.y: int = random.randint(0,100)

    # Add a connection to this node
    def add_connection(self, connection: 'Node'):
        self.connections.append(connection)
    
    def receive(self, incoming_data: int):
        self.incoming_data = incoming_data

    def process(self):
        self.data += self.incoming_data
        self.incoming_data = 0
    
    def send(self):
        # Send a copy of my data
        if len(self.connections) == 1:
            self.connections[0].receive(self.data)
            # Delete my copy of my data only if I send it
            self.data = 0

class NodeMesh:
    def __init__(self, nodes: List[Node] = []):
        self.nodes: List[Node] = nodes
    
    def add_node(self, node: Node):
        self.nodes.append(node)
    
    def step(self):
        for node in self.nodes:
            node.send()
        
        for node in self.nodes:
            node.process()
    
    def get_nodes(self):
        return self.nodes
    
    def __repr__(self):
        node_data: List[int] = [node.data for node in self.nodes]
        return str(node_data)

class Simulation:
    def __init__(self, node_mesh: NodeMesh):
        self.node_mesh: NodeMesh = node_mesh
        self.history: List[NodeMesh] = [copy.deepcopy(self.node_mesh)]

    def run(self, steps: int):
        for _ in range(steps):
            self.node_mesh.step()
            self.history.append(copy.deepcopy(self.node_mesh))

    def get_history(self):
        return self.history