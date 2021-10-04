import unittest
import geometryCalculator

class geometryCalculatorTest(unittest.TestCase):

    #passing tests
    def test_volume1(self):
        assert(geometryCalculator.pick(8))


if __name__ == '__main__':
    unittest.main()