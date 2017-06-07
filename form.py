from great_stocks.selection_model import pick_model
from great_stocks.model_utils import *
from flask_wtf import Form
from wtforms import StringField, PasswordField, TextAreaField, FloatField
from wtforms.validators import (DataRequired, Regexp, ValidationError,
                               Length, EqualTo)

class Entries(Form):
    companyname = StringField(
        "companyname", validators=[
            DataRequired(),
            Regexp(
                r'^[a-zA-Z0-9_]+$, message=("Company Name should be one word, letters, numbers, and underscores only.")
            ), name_exists])
    income = FloatField(
        "income", validators=[
        DataRequired(),
        Regexp(
            r'^[0-9]+$, message=("Income should be numbers only.")
        ), name_exists])
    share_price = FloatField(
        "income", validators=[
        DataRequired(),
        Regexp(
            r'^[0-9]+$, message=("Share Price should be numbers only.")
        ), name_exists])
    total_assets = FloatField(
        "income", validators=[
        DataRequired(),
        Regexp(
            r'^[0-9]+$, message=("Total Assets should be numbers only.")
        ), name_exists])


    """docstring for Entries.Form  def __init__(self, arg):
        super(Entries,Form.__init__()
        self.arg = arg"""
