# In this file, you can find some further analysis that may be helpful for finding a car.

# Imports
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('cleaned_dataframe_for_analysis.csv')

# Get lists of unique feature values for multiselect options in main
def get_multiselect_options():

    options_mileage = data['mileage'].unique()
    options_brand = data['car_brand'].unique()
    options_model = data['model'].unique()
    options_fuel = data['propulsion'].unique()
    options_gear = data['gear'].unique()
    options_hp = data['hp'].unique()
    options_year = data['year_registration'].unique()

    return options_mileage, options_brand,options_model, options_fuel, options_gear, options_hp, options_year

