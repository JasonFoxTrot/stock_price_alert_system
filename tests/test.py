#!/usr/bin/env python3
import unittest
import logging
import coloredlogs
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,str(parentdir) + "/src") 
from tracker_v2 import StockTracker


class TestStockTracker(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.log = logging.getLogger("tracker_test")
        cls.log.level = logging.INFO
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        ch.setFormatter(formatter)
        cls.log.addHandler(ch)
        coloredlogs.install(level=logging.INFO, logger=cls.log)
        cls.st = StockTracker()
        #super(TestStockTracker, self).setUp()

    def test_start(self):
        self.log.info("Starting the tracker... did it crash?")
        self.assertEqual( self.st.start(), True )

    def test_getStockPrice(self):
        self.log.info("Testing getStockPrice() of valid stock.")
        self.assertEqual( isinstance( self.st.getStockPrice('AAPL'), float ), True )
    
    def test_getInvalidStockPrice(self):
        self.log.info("Testing getStockPrice() of invalid stock.")
        self.assertEqual( self.st.getStockPrice('ZEN'), 0.00 )
        
    def test_getBitstampPrice(self):
        self.log.info("Testing getStockPrice() of bitstamp symbol.")
        self.assertEqual( isinstance( self.st.getStockPrice('xrpusd'), float ), True )

if __name__ == '__main__':
    #unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStockTracker)
    unittest.TextTestRunner( verbosity = 0 ).run( suite )