class Node:
    def __init__(self, node_id, data):
        self.node_id = node_id
        self.data = data

    def __repr__(self):
        return f"Node({self.node_id}, {self.data})"

class Condition(Node):
    def __init__(self, node_id, data):
        super().__init__(node_id, data)
        self.type = "condition"

class AndWaypoint(Node):
    def __init__(self, node_id, data):
        super().__init__(node_id, data)
        self.type = "and_waypoint"