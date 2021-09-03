import pytest

from .context import src


class TestBasic:
    def test_truth(self):
        assert True


def equals(a, b):
    assert a == b
