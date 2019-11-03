.. _example:

*******
Example
*******

.. code-block:: python

    from hashlib import sha256
    from merkle_tree_stream import MerkleTreeGenerator

    def leaf(node, roots=None):
        return sha256(node.data).digest()

    def parent(first, second):
        sha256 = hashlib.sha256()
        sha256.update(first.data)
        sha256.update(second.data)
        return sha256.digest()

    merkle = MerkleTreeGenerator(leaf=leaf, parent=parent)
    merkle.write('hello')
    merkle.write('hashed')
    merkle.write('world')
