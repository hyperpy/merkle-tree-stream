"""Merkle tree test module."""

import hashlib

import pytest

from merkle_tree_stream import MerkleTreeIterator, MerkleTreeNode


def test_hashes(leaf, parent):
    merkle_iter = MerkleTreeIterator(leaf=leaf, parent=parent)

    merkle_iter.write(b'a')
    merkle_iter.write(b'b')

    expected_count = 2 + 1  # nodes plus parent
    assert len(merkle_iter) == expected_count

    assert next(merkle_iter) == MerkleTreeNode(
        index=0,
        parent=1,
        hash=hashlib.sha256(b'a').hexdigest(),
        size=1,
        data=b'a',
    )

    assert next(merkle_iter) == MerkleTreeNode(
        index=2,
        parent=1,
        hash=hashlib.sha256(b'b').hexdigest(),
        size=1,
        data=b'b',
    )

    hashed = hashlib.sha256(b'a')
    hashed.update(b'b')

    assert next(merkle_iter) == MerkleTreeNode(
        index=1, parent=3, hash=hashed.hexdigest(), size=2, data=b''
    )

    with pytest.raises(StopIteration):
        next(merkle_iter)


def test_single_root(leaf, parent):
    merkle_iter = MerkleTreeIterator(leaf=leaf, parent=parent)

    merkle_iter.write(b'a')
    merkle_iter.write(b'b')
    merkle_iter.write(b'c')
    merkle_iter.write(b'd')

    assert len(merkle_iter.roots) == 1


def multiple_roots(leaf, parent):
    merkle_iter = MerkleTreeIterator(leaf=leaf, parent=parent)

    merkle_iter.write(b'a')
    merkle_iter.write(b'b')
    merkle_iter.write(b'c')

    assert len(merkle_iter.roots) > 1
