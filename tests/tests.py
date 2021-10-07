'''
Test cases for the suntransit module.
'''

import datetime
import os
import unittest
import numpy as np
from itertools import product
from suntransit import sunrise_sunset

np.seterr(all = 'ignore')

class SunriseSunsetTestSuite(unittest.TestCase):
    '''
    Tests for the sunrise_sunset() function.
    '''
    def test_sunrise_sunset(self):
        coordinates = [
            (42.5, -83.5), (60, -120),
        ]
        dates = [
            datetime.datetime(1969, 7, 20), datetime.datetime(1990, 1, 1),
            datetime.datetime(2000, 7, 20), datetime.datetime(2015, 3, 31),
        ]
        solutions = [ # NOTE: To the nearest hour!
            (10, 1), (13, 22), (10, 1), (11, 23),
            (11, 4), (17, 23), (11, 4), (13, 2)
        ]
        for i, arguments in enumerate(product(coordinates, dates)):
            ss = list(map(np.floor, sunrise_sunset(*arguments)))
            self.assertTrue(np.equal(ss, solutions[i]).all())


if __name__ == '__main__':
    unittest.main()
