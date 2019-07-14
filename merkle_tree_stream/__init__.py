"""merkle-tree-stream module."""

from merkle_tree_stream.generator import (  # noqa
    MerkleTreeGenerator,
    MerkleTreeNode,
)

try:
    import pkg_resources
except ImportError:
    pass


try:
    __version__ = pkg_resources.get_distribution('merkle_tree_stream').version
except Exception:
    __version__ = 'unknown'
