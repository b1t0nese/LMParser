import pytest
from yandex_testing_lesson import count_chars


def test_empty():
    assert count_chars("") == {}


def test_default():
    assert count_chars("123") == {"1": 1, "2": 1, "3": 1}


def test_default2():
    assert count_chars("count_chars") == {
        "c": 2, "o": 1, "u": 1, "n": 1, "t": 1,
        "_": 1, "h": 1, "a": 1, "r": 1, "s": 1}


def test_wrong_type():
    with pytest.raises(TypeError):
        count_chars(42)


def test_wrong_type2():
    with pytest.raises(TypeError):
        count_chars(["123", "123"])
