import unittest
from geometry import distance_between_points


class TestGeometry(unittest.TestCase):

    def test_distance_between_points_2d(self):
        self.assertEqual(distance_between_points((3, 2, 0), (7, 8, 0)), 7.21)
        self.assertEqual(distance_between_points((2, -6, 0), (7, 3, 0)), 10.30)
        self.assertEqual(distance_between_points((7, 5, 0), (3, 2, 0)), 5)

    def test_distance_between_points_3d(self):
        self.assertEqual(distance_between_points((- 2, 3, 5), (1, 2, 3)), 3.74)