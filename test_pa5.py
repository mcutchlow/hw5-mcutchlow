#!/usr/bin/env python3

import math
from os.path import exists

import unittest
from gradescope_utils.autograder_utils.decorators import weight, number

try:
   from pa5 import gcd
except ImportError:
   pass
try:
   from pa5 import remove_pairs
except ImportError:
   pass

try:
    from pa5 import bisection_root
except ImportError:
    pass


class TestHW5(unittest.TestCase):
    def setUp(self):
        pass

    def try_removepairs(self, directions):
        try:
            removed_pairs = remove_pairs(directions)
        except AttributeError as err:
            raise AttributeError("remove_pairs gave exception "+repr(err)) from err
        return(removed_pairs)

    @weight(0)
    @number("0.0")
    def test_exist_pa5(self):
        '''Test pa5.py exists'''
        self.assertTrue(exists("pa5.py"), "pa5.py exists")

    @weight(0)
    @number("3.0")
    def test_run_gcd_defined(self):
        '''Test gcd defined by pa5'''
        self.assertTrue("gcd" in globals(), "gcd not defined")

    @weight(1)
    @number("3.1")
    def test_run_gcd_div0(self):
        '''Test gcd runs with 0,0'''
        gcd(0,0)

    @weight(1)
    @number("3.2")
    def test_run_gcd_1_1(self):
        '''Test gcd runs with 1,1'''
        self.assertEqual(gcd(1,1), 1)

    @weight(1)
    @number("3.3")
    def test_run_gcd(self):
        '''Test gcd runs'''
        gcd(1,1)

    @weight(1)
    @number("3.4")
    def test_run_gcd_zero(self):
        '''Test gcd(7, 11) == 1 '''
        self.assertEqual(gcd(7, 11), 1 , "gcd(7,11)==1")

    @weight(1)
    @number("3.5")
    def test_run_gcd_equal(self):
        '''Test gcd(107, 107) == 107 '''
        self.assertEqual(gcd(107, 107), 107 , "gcd(107,107)==107")

    @weight(2)
    @number("3.6")
    def test_run_gcd_42(self):
        '''Test gcd(294, 378) == 42 '''
        self.assertEqual(gcd(294, 378), 42, "test gcd for correctness")

    @weight(2)
    @number("3.7")
    def test_run_gcd_100237(self):
        '''Test gcd(22352851, 44004043) == 100237 '''
        self.assertEqual(gcd(22352851, 44004043), 100237, "test gcd for correctness")



    @weight(0)
    @number("4.0")
    def test_remove_pairs_exists(self):
        '''remove_pairs defined'''
        self.assertTrue("remove_pairs" in globals(), "remove_pairs not defined")

    @weight(1)
    @number("4.1")
    def test_remove_pairs_runs(self):
        '''remove_pairs runs without error'''
        try:
            remove_pairs("SEESWEW")
        except AttributeError as err:
            raise AttributeError("remove_pairs gave exception "+repr(err)) from err

    @weight(1)
    @number("4.2")
    def test_remove_pairs_22(self):
        '''remove_pairs gives right answer'''
        try:
            removed_pairs = remove_pairs("EEEWWSES")
        except AttributeError as err:
            raise AttributeError("remove_pairs gave exception "+repr(err)) from err
        self.assertEqual(removed_pairs, "EEWSES", "test remove_pairs(EEEWWSES)")

    @weight(1)
    @number("4.22")
    def test_remove_pairs_squared(self):
        '''remove_pairs gives right answer'''
        try:
            removed_pairs = remove_pairs(remove_pairs("EEEWWSES"))
        except AttributeError as err:
            raise AttributeError("remove_pairs gave exception "+repr(err)) from err
        self.assertEqual(removed_pairs, "ESES", "test remove_pairs(EEEWWSES)")

    @weight(1)
    @number("4.23")
    def test_remove_pairs_3(self):
        '''remove_pairs gives right answer'''
        try:
            removed_pairs = remove_pairs("SEESWEW")
        except AttributeError as err:
            raise AttributeError("remove_pairs gave exception "+repr(err)) from err
        self.assertEqual(removed_pairs, "SEESW", "test remove_pairs for correctness")

    @weight(1)
    @number("4.24")
    def test_remove_pairs_5(self):
        '''remove_pairs gives right answer'''
        try:
            removed_pairs = remove_pairs("SWEN")
        except AttributeError as err:
            raise AttributeError("remove_pairs gave exception "+repr(err)) from err
        self.assertEqual(removed_pairs, "SN", "test remove_pairs for correctness")

    @weight(1)
    @number("4.25")
    def test_remove_pairs_NEWS(self):
        '''remove_pairs gives right answer NEWS'''
        self.assertEqual(self.try_removepairs("NEWS"),  "NS", "test remove_pairs for correctness")

    @weight(1)
    @number("4.32")
    def test_remove_pairs_NWES(self):
        '''remove_pairs gives right answer NWES'''
        self.assertEqual(self.try_removepairs("NWES"), "NS", "test remove_pairs for correctness")

    @weight(1)
    @number("4.33")
    def test_remove_pairs_SEWN(self):
        '''remove_pairs gives right answer SEWN'''
        self.assertEqual(self.try_removepairs("SEWN"), "SN", "test remove_pairs for correctness")

    @weight(1)
    @number("4.34")
    def test_remove_pairs_SWEN(self):
        '''remove_pairs gives right answer SWEN'''
        self.assertEqual(self.try_removepairs("SWEN"), "SN", "test remove_pairs for correctness")

    @weight(1)
    @number("4.35")
    def test_remove_pairs_ENSW(self):
        '''remove_pairs gives right answer ENSW'''
        self.assertEqual(self.try_removepairs("ENSW"), "EW", "test remove_pairs for correctness")

    @weight(1)
    @number("4.36")
    def test_remove_pairs_ESNW(self):
        '''remove_pairs gives right answer ESNW'''
        self.assertEqual(self.try_removepairs("ESNW"), "EW", "test remove_pairs for correctness")

    @weight(1)
    @number("4.37")
    def test_remove_pairs_WSNE(self):
        '''remove_pairs gives right answer WSNE'''
        self.assertEqual(self.try_removepairs("WSNE"), "WE", "test remove_pairs for correctness")

    @weight(1)
    @number("4.38")
    def test_remove_pairs_WNSE(self):
        '''remove_pairs gives right answer WNSE'''
        self.assertEqual(self.try_removepairs( "WNSE"), "WE", "test remove_pairs for correctness")

    @weight(1)
    @number("4.39")
    def test_remove_pairs_WNS(self):
        '''remove_pairs gives right answer WNS'''
        self.assertEqual(self.try_removepairs( "WNS"), "W", "test remove_pairs for correctness")

    @weight(1)
    @number("4.391")
    def test_remove_pairs_NSE(self):
        '''remove_pairs gives right answer NSE'''
        self.assertEqual(self.try_removepairs( "NSE"), "E", "test remove_pairs for correctness")

#    @weight(1)
#    @number("4.3")
#    def test_remove_pairs_4(self):
#        '''remove_pairs gives right answer'''
#        self.assertEqual(self.try_removepairs("SWEWEWESS"), "SSS", "test remove_pairs for correctness")

    @weight(1)
    @number("1.0")
    def test_run_bisect(self):
        '''Test bisection_root defined'''
        self.assertEqual("bisection_root" in globals(), True, "bisection_root not defined")

    @weight(1)
    @number("1.1")
    def test_run_bisect1(self):
        '''Test bisection_root runs'''
        bisection_root(math.sin, 2, 4)

    @weight(1)
    @number("1.2")
    def test_run_bisect2(self):
        '''Test bisection_root math.sin '''
        root = bisection_root(math.sin, 2, 4)
        self.assertEqual(abs(root - math.pi) < 1E-6 , True, "bisection_root(math.sin, 2, 4) == pi")

    @weight(1)
    @number("1.3")
    def test_run_bisect3(self):
        '''Test bisection_root linear'''
        root = bisection_root(math.sin, 2, 4)
        self.assertEqual(abs ( bisection_root(lambda x: x - 2.25, 2, 4) - 2.25 ) < 1E-6  ,
                        True, "bisection_root(lambda x: x - 2.25, 2, 4) ==2.25")

    @weight(1)
    @number("1.4")
    def test_run_bisect3(self):
        '''Test bisection_root -linear '''
        root = bisection_root(math.sin, 2, 4)
        self.assertEqual(abs ( bisection_root(lambda x: 1.33 -x, 1, 3) - 1.33 ) < 1E-6  ,
                        True, "bisection_root(lambda x: 1.33 -x , 1, 3) ==1.33")

    @weight(2)
    @number("1.5")
    def test_run_bisect4(self):
        '''Test bisection_root sqrt3'''
        root = bisection_root(lambda x: x*x - 3, 1, 4)
        self.assertEqual(abs ( bisection_root(lambda x: x*x - 3, 1, 4) - math.sqrt(3) ) < 1E-6  ,
                        True, "bisection_root(lambda x: x*x - 3, 1, 4) ==sqrt(3)")


