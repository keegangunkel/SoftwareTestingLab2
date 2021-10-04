import unittest
import cuboid

class cuboidTest(unittest.TestCase):

    #tests that pass
    def test_volume1(self):
        assert(cuboid.volume(5,10,15) ==  750)
        

    def test_volume2(self):
        assert(cuboid.volume(7,69,100) == 48300)
        

    #test that fails
    def test_volume3(self):
        assert(cuboid.volume(5,4,3) == 0)
        


if __name__ == '__main__':
    unittest.main()