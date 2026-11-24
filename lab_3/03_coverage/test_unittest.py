import unittest
from app import Figure


class TestFigureUnittest(unittest.TestCase):
    def test_triangle_angles(self):
        fig = Figure("triangle")
        self.assertEqual(fig.get_angles, 3)


if __name__ == "__main__":
    unittest.main()
