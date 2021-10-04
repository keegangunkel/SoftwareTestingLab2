import unittest
import equilateralTriangle

class equilatealTriangleTest(unittest.TestCase):

    #tests that pass
    def test_volume1(self):
        assert(equilateralTriangle.area(5) ==  10.825317547305483)

    def test_volume2(self):
        assert(equilateralTriangle.area(69) == 2061.573473708856)

    #test that fails
    def test_volume3(self):
        assert(equilateralTriangle.area(6) == 0)



if __name__ == '__main__':
    unittest.main()