# Simple validation tests for the project.
# These are beginner-level tests using only Python's built-in unittest.

import unittest
from utils import get_next_id


class TestProject(unittest.TestCase):

    def test_first_id(self):
        self.assertEqual(get_next_id([]), 1)

    def test_next_id(self):
        items = [
            {"id": 1},
            {"id": 2},
            {"id": 5}
        ]
        self.assertEqual(get_next_id(items), 6)


if __name__ == "__main__":
    unittest.main()
