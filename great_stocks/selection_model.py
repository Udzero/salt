# -*- coding: utf-8 -*-
"""
Created on Tue May 24 20:10:14 2017

@author: Great Stocks Inc.
"""

def pick_model(data):
    """selection model based on a high return on assets as well as a high earning yield criteria.
    """

    for item in data:
        item_avg = calc_average(item['roa'], item['ey'])
        item['avg'] = item_avg

    # order data by avg descending
    ordered_data = sorted(data, key=lambda k: k['avg'], reverse=True)

    return ordered_data[:5]


def calc_average(roa, ey):
    """Calucates the average of the earnings yields and roa
    """
    avg = (ey + roa) / 2
    return avg
