"""A merkle tree node."""

from typing import Any, Optional

import attr
from flat_tree import FlatTreeAccessor

__all__ = ['MerkleTreeNode']


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
    hash: Optional[str] = attr.Factory(str)

    def __attrs_post_init__(self) -> Any:
        """Initialise the parent index."""
        flat_tree = FlatTreeAccessor()
        self.parent = flat_tree.parent(self.index)
