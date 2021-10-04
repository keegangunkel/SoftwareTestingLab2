import unittest
import cube

class cubeTest(unittest.TestCase):

    #tests that pass
    def test_volume1(self):
        assert(cube.volume(5) ==  125)
        assert(cube.surfaceArea(5) == 150 )

    def test_volume2(self):
        assert(cube.volume(69) == 328509)
        assert(cube.surfaceArea(69) == 28566)

    #test that fails
    def test_volume3(self):
        assert(cube.volume(0) == 0)
        assert(cube.surfaceArea(0) == 0)


if __name__ == '__main__':
    unittest.main()