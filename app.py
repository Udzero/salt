# -*- coding: utf-8 -*-
"""
Created on Tue May 23 21:35:50 2017

@author: Great Stocks Inc.
"""

from flask import Flask, render_template, request, redirect
from great_stocks.selection_model import pick_model
from great_stocks.model_utils import *

app = app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/pick-model", methods=['GET', 'POST'])
def select_model():

    if request.method == 'POST':

        # process the user input
        company_results = process_input();

        return render_template('pick_model_results.html', results=company_results)
    else:
        num_of_companies = int(request.args.get('cnt', 2))

        return render_template("select_model_form.html", num=num_of_companies)


def process_input():
    #convert user input into python list
    company_list = {}

    for key, val in request.form.items():
        idx = key[-1]

        if idx not in company_list:
            company_list[idx] = {}

        company_list[idx][key[:-2]] = val

    # Calculate the roa and the ey for each line
    for key, com in company_list.items():
        try:
            roa = return_on_assets(float(com['income']), float(com['totalassets']))
            ey  = earnings_yield(float(com['income']), float(com['shareprice']))
            com['roa'] = roa
            com['ey'] = ey
        except:
            print("Digits only please")

    # useing selection model, order the data by the specified model
    model_results = pick_model(company_list.values())

    return model_results


if __name__ == "__main__":
    app.run()
