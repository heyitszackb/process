from typing import List
from node_mesh import NodeMesh
import copy

class Simulation:
    def __init__(self, node_mesh: NodeMesh) -> None:
        self.node_mesh: NodeMesh = node_mesh
        self.history: List[NodeMesh] = [copy.deepcopy(self.node_mesh)]

    def run(self, steps: int) -> None:
        for _ in range(steps):
            self.node_mesh.step()
            self.history.append(copy.deepcopy(self.node_mesh))

    def get_history(self) -> List[NodeMesh]:
        return self.history
