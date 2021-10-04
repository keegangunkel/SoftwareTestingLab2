import unittest
import equilateralTriangle

class equilatealTriangleTest(unittest.TestCase):

    #tests that pass
    def test_volume1(self):
        assert(equilateralTriangle.area(5) ==  10.83)
        assert(equilateralTriangle.perimeter(5) == 15 )

    def test_volume2(self):
        assert(equilateralTriangle.area(69) == 2061.57)
        assert(equilateralTriangle.perimeter(69) == 207)

    #test that fails
    def test_volume3(self):
        assert(equilateralTriangle.area(0) == 0)
        assert(equilateralTriangle.perimeter(0) == 0)


if __name__ == '__main__':
    unittest.main()