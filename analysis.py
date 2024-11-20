# Imports
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

data = pd.read_csv('cleaned_dataframe_for_analysis.csv')

# Some Transformings:
# Drop first column
data = data.drop(data.columns[0], axis=1) 
# Remove commas as thousand separators in year values
data['year_registration'] = data['year_registration'].astype(str)
data['year_registration'] = data['year_registration'].str.replace(',', '')
data['year_registration'] = data['year_registration'].astype(int) 
# Cast 'hp' into int
data['hp'] = data['hp'].astype('int')
# New column order
new_column_order = ['car_brand', 'model', 'propulsion', 'gear', 'hp', 'mileage', 'year_registration', 'offerType', 'price']
data = data[new_column_order]

# Get multiselect options for car brand
def get_options_brand():
    options_brand = data['car_brand'].unique()
    options_brand.sort()  # Sort list
    return options_brand

# Get multiselect options for model based on selected car brands
def get_options_model(selected_brands):
    data_mapping = {} # dynamic multiselect options list based on car_brand
    options_model = []

    # Group the data by brand and populate the mapping
    for brand, group in data.groupby('car_brand'):
        data_mapping[brand] = {
        'models':group['model'].unique().tolist()
        }
    
    # If no brands selected, include all brands
    if not selected_brands:
        selected_brands = list(data.mapping.keys())

    # Aggregate options for the selected brands
    for brand in selected_brands:
        if brand in data_mapping:
            options_model.extend(data_mapping[brand]['models'])

    # Remove duplicates and sort the options
    return sorted(set(options_model))

# Get multiselect options for propulsion based on selected car brands and models
def get_options_propulsion(selected_brands, selected_models):
    data_mapping = {}     # dynamic multiselect options list based on car_brand and model
    options_fuel = []

    # Group the data by brand + model and pupulate the mapping
    for (brand, model), group in data.groupby(['car_brand','model']):
        if brand not in data_mapping:
            data_mapping[brand] = {}
        data_mapping[brand][model] = {
            'propulsion':group['propulsion'].unique().tolist()
        }
    
    # If no brands and models selected, include all brands and models
    if not selected_brands:
        selected_brands = list(data_mapping.keys())
    if not selected_models:
        selected_models = [model for models in data.mapping.values() for model in models]

    # Aggregate options for selected brands and selected models
    for brand in selected_brands:
        if brand in data_mapping:
            for model in selected_models:
                if model in data_mapping[brand]:
                    options_fuel.extend(data_mapping[brand][model]['propulsion'])

    # Remove duplicates and sort the options
    return sorted(set(options_fuel))

# Get lists of unique feature values for multiselect options in main for filters
def get_multiselect_options(selected_brands):  # dynamic multiselect options list based on car_brand
    data_mapping = {}

    # Group the data by brand and populate the mapping
    for brand, group in data.groupby('car_brand'):
        data_mapping[brand] = {
            'models': group['model'].unique().tolist(),
            'propulsion': group['propulsion'].unique().tolist(),
            'gear': group['gear'].unique().tolist(),
            'hp': group['hp'].unique().tolist(),
            'mileage': group['mileage'].unique().tolist(),
            'year_registration': group['year_registration'].unique().tolist(),
        }

    # Prepare the filtered options based on selected brands
    options_mileage = []
    options_gear = []
    options_hp = []
    options_year = []

    # If no brands are selected, include all brands
    if not selected_brands:
        selected_brands = list(data_mapping.keys())

    # Aggregate options for the selected brands
    for brand in selected_brands:
        if brand in data_mapping:
            options_mileage.extend(data_mapping[brand]['mileage'])
            options_gear.extend(data_mapping[brand]['gear'])
            options_hp.extend(data_mapping[brand]['hp'])
            options_year.extend(data_mapping[brand]['year_registration'])

    # Remove duplicates and sort the options
    return (
        sorted(set(options_mileage)),
        sorted(set(options_gear)),
        sorted(set(options_hp)),
        sorted(set(options_year))
    )

# Provide data 
def provide_data_find(input_mileage_find, input_brand_find, input_model_find, input_fuel_find, input_gear_find, input_hp_find, input_year_find):

    # Filter
    # mileage
    filtered_data = data[(data['mileage'] >= input_mileage_find[0]) & (data['mileage'] < input_mileage_find[1])]
    # car brand
    if input_brand_find:
        filtered_data = filtered_data[filtered_data['car_brand'].isin(input_brand_find)]
    # model
    if input_model_find:
        filtered_data = filtered_data[filtered_data['model'].isin(input_model_find)]
    # Fuel
    if input_fuel_find:
        filtered_data = filtered_data[filtered_data['propulsion'].isin(input_fuel_find)]
    # Gear
    if input_gear_find:
        filtered_data = filtered_data[filtered_data['gear'].isin(input_gear_find)]
    # Hp
    if input_hp_find:
        filtered_data = filtered_data[(filtered_data['hp'] >= input_hp_find[0]) & (filtered_data['hp'] < input_hp_find[1])]
    # Year of Registration
    if input_year_find:
        filtered_data = filtered_data[(filtered_data['year_registration'] >= input_year_find[0]) & (filtered_data['year_registration'] < input_year_find[1])]
    
    # Drop index
    filtered_data = filtered_data.reset_index(drop=True)

    # Prints
    st.write("Filtered Data:")
    st.table(data=filtered_data)
