import random
from typing import List

class Node:
    def __init__(self, data: int = 0) -> None:
        self.size = 6
        self.incoming_data: int = 0
        self.data: int = data
        self.connections: List[Node] = []
        self.x: int = random.randint(0,100)
        self.y: int = random.randint(0,100)

    # Add a connection to this node
    def add_connection(self, connection: 'Node') -> None:
        self.connections.append(connection)
    
    def receive(self, incoming_data: int) -> None:
        self.incoming_data = incoming_data

    def process(self) -> None:
        self.data += self.incoming_data
        self.incoming_data = 0
    
    def send(self) -> None:
        # Send a copy of my data
        if len(self.connections) == 1:
            self.connections[0].receive(self.data)
            # Delete my copy of my data only if I send it
            self.data = 0