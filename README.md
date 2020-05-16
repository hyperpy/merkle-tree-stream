# merkle-tree-stream

[![Build Status](https://drone.autonomic.zone/api/badges/hyperpy/merkle-tree-stream/status.svg)](https://drone.autonomic.zone/hyperpy/merkle-tree-stream)

## A stream that generates a merkle tree based on the incoming data

```sh
$ pip install merkle-tree-stream
```

A hash tree or merkle tree is a tree in which every leaf node is labelled with
the hash of a data block and every non-leaf node is labelled with the
cryptographic hash of the labels of its child nodes. Merkle trees in Dat are
specialized flat trees that contain the content of the archives.
