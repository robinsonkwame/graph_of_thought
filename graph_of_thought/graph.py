from node import Node
from edge import Edge
from checker import Checker

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}

    def create_node(self, data):
        node = Node(
            node_id=len(self.nodes),
            data=data
        )
        self.nodes.add(node)
        return node

    def create_edge(self, from_node, to_node, properties=None):
        edge = Edge(
            from_node, 
            to_node, 
            properties
        )
        self.edges.setdefault(
            from_node, 
            []
        ).append(edge)

    def remove_nodes(self, nodes_to_remove):
        self.nodes.difference_update(nodes_to_remove)
        self.edges = {
            node: edges for node, edges in \
                self.edges.items() if node not in nodes_to_remove
        }

# todo: write update graph