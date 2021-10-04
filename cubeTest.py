import unittest
import cube

class cubeTest(unittest.TestCase):

    #tests that pass
    def test_volume1(self):
        assert(cube.volume(5) ==  125)


    def test_volume2(self):
        assert(cube.volume(69) == 328509)


    #test that fails
    def test_volume3(self):
        assert(cube.volume(9) == 0)



if __name__ == '__main__':
    unittest.main()