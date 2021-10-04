import unittest
import triangle

class triangleTest(unittest.TestCase):

    #tests that pass
    def test_volume1(self):
        assert(triangle.area(5,10,15) ==  0)


    def test_volume2(self):
        assert(triangle.area(20,40,60) == 0)


    #test that fails
    def test_volume3(self):
        assert(triangle.area(8,8,8) == 0)



if __name__ == '__main__':
    unittest.main()