from typing import List, Optional, Union

from node import Node


class TreeGenerator:
    def __init__(self):
        self.nodes_dict = {}
        self.parents_dict = {}
        self.root_node = None

    def generate_tree_from_list(self, nodes_list: List[dict]) -> Node:
        """ Generate Tree from list of dicts
        List element format: dict(id=int, parent=int|str, type=optional[str])"""
        for node in nodes_list:
            self._generate_node(node)

        return self.root_node

    def _generate_node(self, node: dict) -> None:

        node_parent = node.pop("parent")
        node_id = node.pop("id")
        node_instance = Node(node_id=node_id, options=node)

        parent = self._check_parent(node_parent)
        if parent:
            parent.add_child(node_instance)
            node_instance.set_parent(parent)

        for child in self._check_children(node_id):
            node_instance.add_child(child)

        self._update_parents(node_parent, node_instance)
        self._update_nodes(node_id, node_instance)

        if node_parent == 'root':
            self.root_node = node_instance

    def _check_parent(self, node_parent: int) -> Optional[Node]:
        if node_parent in self.nodes_dict:
            parent = self.nodes_dict.get(node_parent)
        else:
            parent = None

        return parent

    def _check_children(self, node_id: dict) -> List[Node]:
        children = []
        if node_id in self.parents_dict:
            children = self.parents_dict.get(node_id)

        return children

    def _update_parents(self, parent_id: int, node_instance: Node) -> None:
        if parent_id in self.parents_dict:
            children = self.parents_dict.get(parent_id)
            children.append(node_instance)
            self.parents_dict[parent_id] = children
        else:
            self.parents_dict.update({parent_id: [node_instance]})

    def _update_nodes(self, node_id: int, node_instance: Node) -> None:
        self.nodes_dict.update({node_id: node_instance})
