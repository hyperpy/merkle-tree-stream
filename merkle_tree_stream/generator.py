"""The merkle tree stream generator."""

from typing import Any, Callable, List, Optional

import attr
from flat_tree import FlatTreeAccessor

__all__ = ['MerkleTreeGenerator', 'MerkleTreeNode']


Hash = str

flat_tree = FlatTreeAccessor()


@attr.s(auto_attribs=True)
class MerkleTreeNode:
    """A node in a merkle tree.

    :param index: TODO
    :param parent: TODO
    :param size: TODO
    :param data: TODO
    :param hash: TODO
    """

    index: int
    parent: Optional[int]
    size: int
    data: bytes
    hash: Optional[str] = None

    def __attrs_post_init__(self) -> Any:
        """Initialise the parent index."""
        self.parent = flat_tree.parent(self.index)


@attr.s(auto_attribs=True)
class MerkleTreeGenerator:
    """A stream that generates a merkle tree based on the incoming data.

    :param leaf: TODO
    :param parent: TODO
    :param roots: TODO
    :param blocks: TODO
    """

    leaf: Callable[[bytes], Hash]
    parent: Callable[[bytes], Hash]
    blocks: int
    roots: Optional[List[MerkleTreeNode]] = attr.Factory(list)

    def next(self, data: bytes) -> List[MerkleTreeNode]:
        """Further generate the treem based on the incoming data.

        :param data: Incoming data
        """
        pass

    def __attrs_post_init__(self) -> Any:
        """Initialise parent and block defaults."""
        for root in self.roots:
            if not root.parent:
                root.parent = flat_tree.parent(root.index)

        # https://github.com/mafintosh/merkle-tree-stream/blob/master/generator.js#L14
        # self.roots[self.roots.length] ...
        # self.blocks = (1 + (flat_tree.right_span(...) / 2)) if self.roots else 0
