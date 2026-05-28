import unittest
from yandex_testing_lesson import reverse


class TestReverse(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(reverse(""), "")

    def test_wrong_type(self):
        with self.assertRaises(TypeError):
            reverse(42)

    def test_wrong_type2(self):
        with self.assertRaises(TypeError):
            reverse([523, 324])

    def test_default(self):
        self.assertEqual(reverse("123"), "321")

    def test_palindrom(self):
        self.assertEqual(reverse("978879"), "978879")

    def test_one_symbol(self):
        self.assertEqual(reverse("1"), "1")


if __name__ == "__main__":
    unittest.main()