import unittest
import trapezoid

class trapezoidTest(unittest.TestCase):

    #tests that pass
    def test_volume1(self):
        assert(trapezoid.area(5,10,15) ==  112.5)
        assert(trapezoid.median(5,10,15) == 7.5 )

    def test_volume2(self):
        assert(trapezoid.area(7,69,100) == 3800)
        assert(trapezoid.median(7,69,100) == 38)

    #test that fails
    def test_volume3(self):
        assert(trapezoid.volume(0,0,0) == 0)
        assert(trapezoid.surfaceArea(0,0,0) == 0)


if __name__ == '__main__':
    unittest.main()