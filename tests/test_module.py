import unittest
<<<<<<< HEAD
# from src.Radial_bias_Raunak_gola import module
from Radial_bias_Raunak_gola import module

=======
from Radial_bias_Raunak_gola import add
>>>>>>> 3401c936d6465bdb05b753f835384a009523272c

class TestAddFunction(unittest.TestCase):
    def test_add(self):
        self.assertEqual(module.add(1, 2), 3)
        self.assertEqual(module.add(-1, 1), 0)
        self.assertEqual(module.add(-1, -1), -2)

if __name__ == '__main__':
    unittest.main()
