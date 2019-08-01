import hashlib

import pytest


@pytest.fixture
def leaf():
    def _leaf(node, roots=None):
        return hashlib.sha256(node.data).hexdigest()

    return _leaf


@pytest.fixture
def parent():
    def _parent(first, second):
        sha256 = hashlib.sha256()
        sha256.update(first.data)
        sha256.update(second.data)
        return sha256.hexdigest()

    return _parent
