import pytest
from yandex_testing_lesson import is_under_queen_attack


def test_empty():
    with pytest.raises(ValueError):
        is_under_queen_attack("", "")


def test_wrong_input():
    with pytest.raises(ValueError):
        is_under_queen_attack("123", "ewr")


def test_default():
    assert is_under_queen_attack("h8", "a1") is True


def test_default2():
    assert is_under_queen_attack("h8", "b1") is False


def test_default3():
    assert is_under_queen_attack("h8", "e5") is True


def test_wrong_type():
    with pytest.raises(TypeError):
        is_under_queen_attack(0, "")