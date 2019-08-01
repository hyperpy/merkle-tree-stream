"""Generator test module."""

import hashlib

from merkle_tree_stream import MerkleTreeGenerator, MerkleTreeNode


def test_hashes(leaf, parent):
    stream = MerkleTreeGenerator(leaf=leaf, parent=parent)

    stream.next(b'a')

    first_node = (
        MerkleTreeNode(
            index=0,
            parent=1,
            hash=hashlib.sha256(b'a').hexdigest(),
            size=1,
            data=b'a',
        ),
    )

    stream.next(b'b')

    second_node = (
        MerkleTreeNode(
            index=2,
            parent=1,
            hash=hashlib.sha256(b'b').hexdigest(),
            size=1,
            data=b'a',
        ),
    )

    stream.next(b'c')

    third = hashlib.sha256(b'a')
    third.update(b'b')
    third_hash = third.hexdigest()

    third_node = (
        MerkleTreeNode(index=1, parent=3, hash=third_hash, size=2, data=b'a'),
    )

    assert stream.nodes == [first_node, second_node, third_node]


def test_single_root(leaf, parent):
    stream = MerkleTreeGenerator(leaf=leaf, parent=parent)

    stream.next('a')
    stream.next('b')
    stream.next('c')
    stream.next('d')

    assert stream.roots.length == 1


def multiple_roots(leaf, parent):
    stream = MerkleTreeGenerator(leaf=leaf, parent=parent)

    stream.next('a')
    stream.next('b')
    stream.next('c')

    assert stream.roots.length > 1
