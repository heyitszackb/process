class DragManager:
    def __init__(self, model):
        self.model = model
        self.dragging = False
        self.drag_offset_x = 0
        self.drag_offset_y = 0
        self.dragged_node = None

    def handle_drag(self, mouse_x, mouse_y, is_mouse_down):
        if is_mouse_down:
            if not self.dragging:
                self.start_drag(mouse_x, mouse_y)
            else:
                self.continue_drag(mouse_x, mouse_y)
        else:
            if self.dragging:
                self.end_drag()

    def start_drag(self, mouse_x, mouse_y):
        self.dragging = False
        self.dragged_node = None
        for node in self.model.get_mesh().get_nodes():
            if self.is_mouse_over_node(mouse_x, mouse_y, node):
                self.dragging = True
                self.dragged_node = node
                self.drag_offset_x = node.x - mouse_x
                self.drag_offset_y = node.y - mouse_y
                break  # Only drag the first node we find

    def continue_drag(self, mouse_x, mouse_y):
        if self.dragging and self.dragged_node:
            self.dragged_node.x = mouse_x + self.drag_offset_x
            self.dragged_node.y = mouse_y + self.drag_offset_y

    def end_drag(self):
        self.dragging = False
        self.dragged_node = None

    @staticmethod
    def is_mouse_over_node(mouse_x, mouse_y, node):
        return (node.x <= mouse_x <= node.x + 10 and
                node.y <= mouse_y <= node.y + 10)