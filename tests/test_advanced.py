import pytest
from tests import equals, src


class TestFoo:
    def test_get_foo(self):
        result = src.get_foo()
        expected = "foo"
        equals(result, expected)

    def test_func(self):
        result = src.func()
        expected = "bar"
        equals(result, expected)


if __name__ == "__main__":
    pytest.main()
