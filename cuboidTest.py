import unittest
import cuboid

class cuboidTest(unittest.TestCase):

    #tests that pass
    def test_volume1(self):
        assert(cuboid.volume(5,10,15) ==  750)
        assert(cuboid.surfaceArea(5,10,15) == 550 )

    def test_volume2(self):
        assert(cuboid.volume(7,69,100) == 16166)
        assert(cuboid.surfaceArea(7,69,100) == 48300)

    #test that fails
    def test_volume3(self):
        assert(cuboid.volume(0,0,0) == 0)
        assert(cuboid.surfaceArea(0,0,0) == 0)


if __name__ == '__main__':
    unittest.main()