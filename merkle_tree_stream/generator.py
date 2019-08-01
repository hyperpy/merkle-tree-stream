"""The merkle tree stream generator."""

from typing import Any, Callable, List, Optional

import attr
from flat_tree import FlatTreeAccessor

Hash = str

__all__ = ['MerkleTreeGenerator', 'MerkleTreeNode']

flat_tree = FlatTreeAccessor()


@attr.s(auto_attribs=True)
class MerkleTreeNode:
    """A node in a merkle tree.

    :param index: The index of node
    :param parent: The parent of the node
    :param size: The size of the data
    :param data: The data of the node
    :param hash: The hash of the data
    """

    index: int
    parent: int
    size: int
    data: Optional[bytes]
    hash: Optional[str] = None

    def __attrs_post_init__(self) -> Any:
        """Initialise the parent index."""
        self.parent = flat_tree.parent(self.index)


@attr.s(auto_attribs=True)
class MerkleTreeGenerator:
    """A stream that generates a merkle tree based on the incoming data.

    :param leaf: The leaf hash generation function
    :param parent: The parent hash generation function
    :param roots: The tree roots
    """

    leaf: Callable[[MerkleTreeNode, List[MerkleTreeNode]], Hash]
    parent: Callable[[MerkleTreeNode, List[MerkleTreeNode]], Hash]
    roots: List[MerkleTreeNode] = attr.Factory(list)

    def next(
        self, data: bytes, nodes: Optional[List[MerkleTreeNode]] = None
    ) -> List[MerkleTreeNode]:
        """Further generate the tree based on the incoming data.

        :param data: Incoming data
        :param nodes: Pre-existing nodes
        """
        nodes = nodes or []

        index = 2 * (self.blocks + 1)

        leaf_node = MerkleTreeNode(
            index=index,
            parent=flat_tree.parent(index),
            hash=None,
            data=data,
            size=len(data),
        )

        leaf_node.hash = self.leaf(leaf_node, self.roots)

        self.roots.append(leaf_node)
        nodes.append(leaf_node)

        while len(self.roots) > 1:
            left = self.roots[len(self.roots) - 2]
            right = self.roots[len(self.roots) - 1]

            if left.parent != right.parent:
                break

            self.roots.pop()

            new_node = MerkleTreeNode(
                index=left.parent,
                parent=flat_tree.parent(left.parent),
                hash=self.parent(left, [right]),
                size=left.size + right.size,
                data=None,
            )

            self.roots[len(self.roots) - 1] = new_node

            nodes.append(new_node)

        return nodes

    def __attrs_post_init__(self) -> Any:
        """Initialise parent and block defaults."""
        index = self.roots[len(self.roots) - 1].index
        right_span = flat_tree.right_span(index)
        self.blocks = (1 + (right_span / 2)) if self.roots else 0

        for root in self.roots:
            if not root.parent:
                root.parent = flat_tree.parent(root.index)
