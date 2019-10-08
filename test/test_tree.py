"""Merkle tree test module."""

import hashlib

import pytest

from merkle_tree_stream import MerkleTreeGenerator, MerkleTreeNode


def test_hashes(leaf, parent):
    merkle = MerkleTreeGenerator(leaf=leaf, parent=parent)

    merkle.write(b'a')
    merkle.write(b'b')

    expected_count = 2 + 1  # nodes plus parent
    assert len(merkle) == expected_count

    assert next(merkle) == MerkleTreeNode(
        index=0, parent=1, hash=hashlib.sha256(b'a').digest(), size=1, data=b'a'
    )

    assert next(merkle) == MerkleTreeNode(
        index=2, parent=1, hash=hashlib.sha256(b'b').digest(), size=1, data=b'b'
    )

    hashed = hashlib.sha256(b'a')
    hashed.update(b'b')

    assert next(merkle) == MerkleTreeNode(
        index=1, parent=3, hash=hashed.digest(), size=2, data=b''
    )

    with pytest.raises(StopIteration):
        next(merkle)


def test_single_root(leaf, parent):
    merkle = MerkleTreeGenerator(leaf=leaf, parent=parent)

    merkle.write(b'a')
    merkle.write(b'b')
    merkle.write(b'c')
    merkle.write(b'd')

    assert len(merkle.roots) == 1


def multiple_roots(leaf, parent):
    merkle = MerkleTreeGenerator(leaf=leaf, parent=parent)

    merkle.write(b'a')
    merkle.write(b'b')
    merkle.write(b'c')

    assert len(merkle.roots) > 1
