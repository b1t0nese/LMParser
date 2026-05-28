import pytest
from yandex_testing_lesson import reverse


def test_empty():
    assert reverse("") == ""


def test_wrong_type():
    with pytest.raises(TypeError):
        reverse(42)


def test_wrong_type2():
    with pytest.raises(TypeError):
        reverse([523, 324])


def test_default():
    assert reverse("123") == "321"


def test_palindrom():
    assert reverse("978879") == "978879"


def test_one_symbol():
    assert reverse("1") == "1"
