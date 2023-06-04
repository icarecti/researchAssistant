from typing import List, Optional

from domain.CanvasNode import CanvasNode


class Canvas:
    def __init__(self, nodes: Optional[List[CanvasNode]] = None, edges: Optional[List[str]] = None):
        self.nodes = nodes if nodes is not None else []
        self.edges = edges if edges is not None else []

    def add_node(self, node: CanvasNode) -> None:
        self.nodes.append(node)

    def add_edge(self, edge: str) -> None:
        self.edges.append(edge)

    def to_dict(self) -> dict:
        return {
            "nodes": [node.to_dict() for node in self.nodes],
            "edges": self.edges
        }
