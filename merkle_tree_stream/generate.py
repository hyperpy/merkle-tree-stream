"""The merkle tree stream generator."""

from typing import Any, Callable, Iterator, List, Optional

import attr
from flat_tree import FlatTreeAccessor

Hash = str

__all__ = ['MerkleTreeIterator', 'MerkleTreeNode']

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
    data: bytes
    hash: Optional[str] = None

    def __attrs_post_init__(self) -> Any:
        """Initialise the parent index."""
        self.parent = flat_tree.parent(self.index)


@attr.s(auto_attribs=True)
class MerkleTreeIterator:
    """A merkle tree iterator based on incoming data.

    :param leaf: The leaf hash generation function
    :param parent: The parent hash generation function
    :param roots: The tree roots
    """

    leaf: Callable[[MerkleTreeNode], Hash]
    parent: Callable[[MerkleTreeNode, MerkleTreeNode], Hash]
    roots: List[MerkleTreeNode] = attr.Factory(list)

    _position: int = 0
    _nodes: List[MerkleTreeNode] = attr.Factory(list)

    def __attrs_post_init__(self) -> Any:
        """Initialise parent and block defaults."""
        try:
            index = self.roots[len(self.roots) - 1].index
        except IndexError:
            index = 0

        right_span = flat_tree.right_span(index)
        self.blocks = (1 + (right_span / 2)) if self.roots else 0

        for root in self.roots:
            if not root.parent:
                root.parent = flat_tree.parent(root.index)

    def __iter__(self) -> Iterator:
        """The iterator initialisation."""
        return self

    def __next__(self) -> MerkleTreeNode:
        """The following node."""
        try:
            node = self._nodes[self._position]
        except IndexError:
            raise StopIteration

        self._position += 1

        return node

    def __len__(self) -> int:
        """The number of nodes stored in the tree."""
        return len(self._nodes)

    def write(self, data: bytes):
        """Write a new node to the tree.

        :param data: The new tree data
        """
        index = 2 * self.blocks

        self.blocks += 1

        leaf_node = MerkleTreeNode(
            index=index,
            parent=flat_tree.parent(index),
            hash=None,
            data=data,
            size=len(data),
        )
        leaf_node.hash = self.leaf(leaf_node)

        self.roots.append(leaf_node)
        self._nodes.append(leaf_node)

        while len(self.roots) > 1:
            left = self.roots[len(self.roots) - 2]
            right = self.roots[len(self.roots) - 1]

            if left.parent != right.parent:
                break

            self.roots.pop()

            new_node = MerkleTreeNode(
                index=left.parent,
                parent=flat_tree.parent(left.parent),
                hash=self.parent(left, right),
                size=left.size + right.size,
                data=b'',
            )

            self.roots[len(self.roots) - 1] = new_node

            self._nodes.append(new_node)
