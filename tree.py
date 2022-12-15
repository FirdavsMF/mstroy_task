from typing import List

from generator import TreeGenerator
from node import Node


class TreeStore:
    def __init__(self, nodes_list: List[dict]) -> None:
        generator = TreeGenerator()
        self._tree = generator.generate_tree_from_list(nodes_list)
        self._nodes_dict = generator.nodes_dict
        self._parents_dict = generator.parents_dict

    def get_all(self) -> List[dict]:
        return self._get_tree_list(self._tree)

    def get_item(self, node_id: int) -> dict:
        node = self._get_node(node_id)
        return node.to_dict()

    def get_children(self, node_id: int) -> List[dict]:
        node = self._get_node(node_id)
        children = node.children
        return [child.to_dict() for child in children]

    def get_all_parents(self, node_id: int) -> List[dict]:
        node = self._get_node(node_id)
        parent = node.parent
        parents_list = []
        while parent != "root":
            parents_list.append(parent.to_dict())
            parent = parent.parent
        return parents_list

    def _get_node(self, node_id: int) -> Node:
        return self._nodes_dict.get(node_id)

    def _get_tree_list(self, node: Node) -> List[dict]:
        tree_list = [node.to_dict()]
        for child in node.children:
            tree_list += self._get_tree_list(child)

        return tree_list
