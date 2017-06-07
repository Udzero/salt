# -*- coding: utf-8 -*-

"""
"""

def return_on_assets(income, total_assets ):
    try:
        roa = income / total_assets
        return roa
    except:
        print("Enter digits only")



def earnings_yield(income, share_price):
    try:
        ey = income / share_price
        return ey
    except:
        print("Enter digits only") 



if __name__ == "__main__":
    pass
