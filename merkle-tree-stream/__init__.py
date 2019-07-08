"""merkle-tree-stream module."""

try:
    import pkg_resources
except ImportError:
    pass


try:
    __version__ = pkg_resources.get_distribution('merkle-tree-stream').version
except Exception:
    __version__ = 'unknown'
