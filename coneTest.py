import unittest
import cone

class coneTest(unittest.TestCase):
    
    #tests that pass
    def test_volume1(self):
        assert(cone.volume(5,10) ==  261.79938779914943)


    def test_volume2(self):
        assert(cone.volume(7,69) == 3540.5749205956963)


    #test that fails
    def test_volume3(self):
        assert(cone.volume(2,3) == 0)



if __name__ == '__main__':
    unittest.main()