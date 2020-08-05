# merkle-tree-stream

[![Build Status](https://drone.autonomic.zone/api/badges/hyperpy/merkle-tree-stream/status.svg)](https://drone.autonomic.zone/hyperpy/merkle-tree-stream)

## A stream that generates a merkle tree based on the incoming data

> A hash tree or merkle tree is a tree in which every leaf node is labelled
> with the hash of a data block and every non-leaf node is labelled with the
> cryptographic hash of the labels of its child nodes. Merkle trees in Dat are
> specialized flat trees that contain the content of the archives.

## Install

```sh
$ pip install merkle-tree-stream
```

## Example

```python
import hashlib

from merkle_tree_stream import MerkleTreeGenerator


def _leaf(node, roots=None):
    return hashlib.sha256(node.data).digest()


def _parent(first, second):
    sha256 = hashlib.sha256()
    sha256.update(first.data)
    sha256.update(second.data)
    return sha256.digest()


merkle = MerkleTreeGenerator(leaf=_leaf, parent=_parent)

merkle.write(b"a")
merkle.write(b"b")

print(merkle._nodes)
```

Output:

```sh
[
 MerkleTreeNode(index=0, parent=1, size=1, data=b'a', hash=b'...'),
 MerkleTreeNode(index=2, parent=1, size=1, data=b'b', hash=b'...'),
 MerkleTreeNode(index=1, parent=3, size=2, data=b'', hash=b'...')
]
```
