"""Tests for django module."""

import pytest  # pylint disable=unused-import


@pytest.mark.parametrize("param", ["a", "b", "c"])
def test_hello_world(param: str) -> None:
    """Blank dummy test."""
    assert param
