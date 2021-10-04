import unittest
import cone

class coneTest(unittest.TestCase):

    #tests that pass
    def test_volume1(self):
        assert(cone.volume(5,10) ==  261.8)
        assert(cone.surfaceArea(5,10) == 254.16 )

    def test_volume2(self):
        assert(cone.volume(7,69) == 1679.12)
        assert(cone.surfaceArea(7,69) == 3540.57)

    #test that fails
    def test_volume3(self):
        assert(cone.volume(0,0) == 0)
        assert(cone.surfaceArea(0,0) == 0)


if __name__ == '__main__':
    unittest.main()