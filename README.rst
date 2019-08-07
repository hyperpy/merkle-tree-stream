.. _header:

******************
merkle-tree-stream
******************

.. image:: https://img.shields.io/badge/license-MIT-brightgreen.svg
   :target: LICENSE
   :alt: Repository license

.. image:: https://badge.fury.io/py/merkle-tree-stream.svg
   :target: https://badge.fury.io/py/merkle-tree-stream
   :alt: PyPI package

.. image:: https://travis-ci.com/datpy/merkle-tree-stream.svg?branch=master
   :target: https://travis-ci.com/datpy/merkle-tree-stream
   :alt: Travis CI result

.. image:: https://readthedocs.org/projects/merkle-tree-stream/badge/?version=latest
   :target: https://merkle-tree-stream.readthedocs.io/en/latest/
   :alt: Documentation status

.. image:: https://img.shields.io/badge/support-maintainers-brightgreen.svg
   :target: https://decentral1.se
   :alt: Support badge

.. _introduction:

A stream that generates a merkle tree based on the incoming data
----------------------------------------------------------------

From `The Dat Protocol`_: 

.. _The Dat Protocol: https://datprotocol.github.io/book/ch01-01-flat-tree.html

    A hash tree or merkle tree is a tree in which every leaf node is labelled
    with the hash of a data block and every non-leaf node is labelled with the
    cryptographic hash of the labels of its child nodes. Merkle trees in Dat
    are specialized `flat trees`_ that contain the content of the archives.

    .. _Flat Trees: https://flat-tree.readthedocs.io/en/latest/

See the following for more:

  * The Dat Protocol: `Merkle Tree`_
  * The Dat Protocol: `Merkle Tree Stream`_

.. _Merkle Tree: https://datprotocol.github.io/book/ch01-02-merkle-tree.html
.. _Merkle Tree Stream: https://datprotocol.github.io/book/ch02-02-merkle-tree-stream.html

A note on naming
================

For the purposes of uniformity and easy of discovery alongside the reference
implementation, we use the same module name as `merkle-tree-stream`_. This may
cause confusion since it is not clear what exactly is referred to when using
the term "stream" in the context of Python. To be clear, this module provides a
`Python iterator`_ which appears to match the implementation and meaning of the
reference implementation.

.. _merkle-tree-stream: https://github.com/mafintosh/merkle-tree-stream
.. _Python iterator: https://docs.python.org/3/c-api/iter.html

.. _documentation:

Documentation
*************

* https://merkle-tree-stream.readthedocs.io/

Mirroring
*********

* https://hack.decentral1.se/datpy/merkle-tree-stream (primary)
* https://github.com/datpy/merkle-tree-stream
