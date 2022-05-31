import unittest
from calculus import lim


class TestCalculus(unittest.TestCase):
    
    def test_limits(self):
        def f(x: float) -> float:
            return (x**2 - 1) / (x - 1)

        def g(x: float) -> float:
            return 2*x - 1
        
        self.assertEqual(lim(f, 1), 2)
        self.assertEqual(lim(g, 3), 5)
