import unittest
import triangle

class triangleTest(unittest.TestCase):

    #tests that pass
    def test_volume1(self):
        assert(triangle.area(5,10,15) ==  30)
        assert(triangle.perimeter(5,10,15) == 0 )

    def test_volume2(self):
        assert(triangle.area(20,40,60) == 0)
        assert(triangle.perimeter(20,40,60) == 120)

    #test that fails
    def test_volume3(self):
        assert(triangle.area(0) == 0,0,0)
        assert(triangle.perimeter(0) == 0,0,0)


if __name__ == '__main__':
    unittest.main()