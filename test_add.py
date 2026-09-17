import unittest
from add import add


class TestAdd(unittest.TestCase):
    def test_add_1_2(self):
        self.assertEqual(add(1, 2), 3)


if __name__ == "__main__":
    unittest.main()
