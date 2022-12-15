from typing import List, Optional


class Node:
    def __init__(self, node_id: int,
                 parent: "Node" = None,
                 children: List["Node"] = None,
                 options: Optional[dict] = None
                 ) -> None:
        if parent is None:
            parent = "root"
        if children is None:
            children = []

        self.node_id = node_id
        self.parent = parent
        self.options = options
        self.children = children

    def add_child(self, child: "Node") -> None:
        self.children.append(child)

    def add_child_from_id(self, child_id: id) -> None:
        self.children.append(self.__class__(child_id, self))

    def set_parent(self, parent: "Node") -> None:
        self.parent = parent

    def to_dict(self) -> dict:
        return {"id": self.node_id,
                "parent": "root" if isinstance(self.parent, str) else self.parent.node_id,
                **self.options}

    def __repr__(self):
        return "<Node %d>" % self.node_id

