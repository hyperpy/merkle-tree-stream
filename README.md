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

def _leaf(node, roots=None):
    return hashlib.sha256(node.data).digest()

def _parent(first, second):
    sha256 = hashlib.sha256()
    sha256.update(first.data)
    sha256.update(second.data)
    return sha256.digest()

merkle = MerkleTreeGenerator(leaf=leaf, parent=parent)

merkle.write(b"a")
merkle.write(b"b")

assert len(merkle) == 2 + 1
```
