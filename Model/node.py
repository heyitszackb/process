import random
from typing import List
import math

class Node:
    def __init__(self, data: int = 0) -> None:
        self.size = 6
        self.incoming_data: int = 0
        self.data: int = data
        self.connections: List[Node] = []
        self.x: int = random.randint(0,100)
        self.y: int = random.randint(0,100)
        self.is_selected = False

    # Add a connection to this node
    def add_connection(self, connection: 'Node') -> None:
        if connection in self.connections:
            return
        else:
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
    
    def is_mouse_over(self, mouse_x: int, mouse_y: int) -> bool:
        # Calculate the distance between the mouse and the center of the node
        distance = math.sqrt((mouse_x - self.x)**2 + (mouse_y - self.y)**2)
        # Check if the distance is less than or equal to the radius
        return distance <= self.size

    def toggle_is_selected(self):
        self.is_selected = not self.is_selected