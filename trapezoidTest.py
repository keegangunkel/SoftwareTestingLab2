import unittest
import trapezoid

class trapezoidTest(unittest.TestCase):

    #tests that pass
    def test_volume1(self):
        assert(trapezoid.area(5,10,15) ==  112.5)

    def test_volume2(self):
        assert(trapezoid.area(7,69,100) == 3800)


    #test that fails
    def test_volume3(self):
        assert(trapezoid.area(3,6,9) == 0)



if __name__ == '__main__':
    unittest.main()