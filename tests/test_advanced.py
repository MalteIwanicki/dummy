import pytest

from .context import src


class TestFoo:
    def test_get_foo(self):
        result = src.get_foo()
        expected = "foo"
        equals(result, expected)

    def test_func(self):
        result = src.func()
        expected = "bar"
        equals(result, expected)


def equals(a, b):
    assert a == b


if __name__ == "__main__":
    pytest.main()
