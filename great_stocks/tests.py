# -*- coding: utf-8 -*-

import unittest
from model_utils import *
from selection_model import *

class ModelUtilsTests(unittest.TestCase):
    
    def test_return_on_assets_ints(self):
        """Test for integer input parameters """
        
        # Preparation
        income = 1
        total_assets = 2
        
        # Execution
        roa_results = return_on_assets(income, total_assets)
        
        #Verification
        self.assertEqual(0.5, roa_results)
    

    def test_return_on_assets(self):
        """Test for floating point input parameters """
        
        # Preparation
        income = 1.0
        total_assets = 2.0
        
        # Execution
        roa_results = return_on_assets(income, total_assets)
        
        #Verification
        self.assertEqual(0.5, roa_results)
    

    def test_earnings_yield_ints(self):
        """Test for integer input parameters """
        
        # Preparation
        income = 5
        share_price = 2
        
        # Execution
        ey_results = earnings_yield(income, share_price)
        
        #Verification
        self.assertEqual(2.5, ey_results)


class ModelSelectionTests(unittest.TestCase):
    
    def test_calc_average(self):
        # prepare
        roa = 0.15
        ey = 2.10
        
        # execution
        avg_res = calc_average(roa, ey)
        
        # verification
        self.assertEqual(1.125, avg_res)


    def test_pick_model(self):
        # prepare 
        data = [
                {'roa': 0.01, 'ey': 0.1, 'cn':'Company A' },
                {'roa': 0.015384615, 'ey': 0.153846154, 'cn':'Company B' },
                {'roa': 0.015, 'ey': 0.15, 'cn':'Company C' },
                {'roa': 0.020588235, 'ey': 0.145833333, 'cn':'Company D' }
                ]
        
        # execution
        pick_results = pick_model(data)
        
        # verification
        self.assertEqual('Company B', pick_results[0]['cn'])
        self.assertEqual('Company A', pick_results[-1]['cn'])        

if __name__ == "__main__":
    unittest.main()
