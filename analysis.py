# In this file, you can find some further analysis that may be helpful for finding a car.

# Imports
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('cleaned_dataframe_for_analysis.csv')

data

# Get lists of unique feature values for multiselect options in main
options_mileage = [0,1000]
options_brand = []
options_model = []
options_fuel = []
options_gear = []
options_hp = []
options_year = [2011,2021]