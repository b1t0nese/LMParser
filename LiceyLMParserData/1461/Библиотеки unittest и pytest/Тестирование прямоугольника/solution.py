import pytest
from yandex_testing_lesson import Rectangle


def test_has_method():
    Rectangle(0, 0).get_area()


def test_has_method2():
    Rectangle(0, 0).get_perimeter()


def test_empty():
    assert Rectangle(0, 0).get_area() == 0


def test_empty2():
    assert Rectangle(0, 0).get_perimeter() == 0


def test_wrong_input():
    with pytest.raises(ValueError):
        Rectangle(-100, 0)


def test_wrong_input2():
    with pytest.raises(ValueError):
        Rectangle(100, -10)


def test_wrong_type():
    with pytest.raises(TypeError):
        Rectangle(0, "213")


def test_wrong_type2():
    with pytest.raises(TypeError):
        Rectangle("0", 213)


def test_default():
    assert Rectangle(6, 6).get_area() == 36


def test_default2():
    assert Rectangle(6, 16).get_area() == 96


def test_default3():
    assert Rectangle(6, 6).get_perimeter() == 24


def test_default4():
    assert Rectangle(6, 10).get_perimeter() == 32