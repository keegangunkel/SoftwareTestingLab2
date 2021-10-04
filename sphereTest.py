import unittest
import sphere

class sphereTest(unittest.TestCase):

    #tests that pass
    def test_volume1(self):
        assert(sphere.volume(5) ==  523.5987755982989)
        assert(sphere.surfaceArea(5) == 314.1592653589793 )

    def test_volume2(self):
        assert(sphere.volume(69) == 1376055.2813841724)
        assert(sphere.surfaceArea(69) == 59828.49049496402)

    #test that fails
    def test_volume3(self):
        assert(sphere.volume(0) == 0)
        assert(sphere.surfaceArea(0) == 0)


if __name__ == '__main__':
    unittest.main()