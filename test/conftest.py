import hashlib

import pytest


@pytest.fixture
def leaf():
    def _leaf(node):
        return hashlib.sha256(leaf.data).hexdigest()

    return _leaf


@pytest.fixture
def parent():
    def _parent(left, right):
        sha256 = hashlib.sha256()
        sha256.update(left)
        sha256.update(right)
        return sha256.hexdigest()

    return _parent
