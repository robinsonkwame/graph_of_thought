class Edge:
    def __init__(self, from_node, to_node, properties=None):
        if properties is None:
            properties = {}
        self.from_node = from_node
        self.to_node = to_node
        self.properties = properties