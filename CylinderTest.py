import unittest
import cylinder

class cylinderTest(unittest.TestCase):

    #tests that pass
    def test_volume1(self):
        assert(cylinder.volume(5,10) == 785.3981633974483)

    def test_volume2(self):
        assert(cylinder.volume(7,69) == 10621.724761787089)
    #test that fails
    def test_volume3(self):
        assert(cylinder.volume(7,69) == 0)

if __name__ == '__main__':
    unittest.main()